from installed_clients2.execution_engine2Client import execution_engine2 as EE2Client
import os
import datetime
import client as c
import filter
import check_keys_with_wsid
token = os.environ['USER_TOKEN']
ee2 = EE2Client(url='https://kbase.us/services/ee2',token=token)
yesterday = (datetime.date.today() - datetime.timedelta(days=1))


def get_errored_apps(start_date=datetime.datetime.combine(yesterday, datetime.datetime.min.time()),
                     end_date=datetime.datetime.combine(yesterday, datetime.datetime.max.time())):
    """This function submits error logs to Logstash. First a call to EE2 is made and app logs 
    that have a job state of 'error' are collected
    At which point a dictionary is initiated which contains basic info that needs to filled 
    in by info from the errored app log.
    After making sure basic fields exist, such as work space id or 'wsid', the beginning 
    dictionary and the errored app log are sent to filter.filter_error so other keys can 
    be checked and the error itself categorized and made readable."""

    if isinstance(start_date, str):
        # Format date strings to datetime objects
        start_date_dt = datetime.datetime.strptime(start_date, '%m-%d-%Y')
        start_date_min = datetime.datetime.combine(start_date_dt, datetime.datetime.min.time())
        end_date_dt = datetime.datetime.strptime(end_date, '%m-%d-%Y')
        end_date_max = datetime.datetime.combine(end_date_dt, datetime.datetime.max.time())
        # datetime to epoch. Epoch format needed for elastic query
        epoch_finish_begin = float(start_date_min.strftime('%s'))
        epoch_end = float(end_date_max.strftime('%s'))
    else:
        # datetime to epoch. Epoch format needed for elastic query
        epoch_finish_begin = float(start_date.strftime('%s'))
        epoch_end = float(end_date.strftime('%s'))
    # the start date range needs to go back 14 days for long running jobs that have not finished yet
    epoch_start_begin = (epoch_finish_begin - (14 * 24 * 60 * 60))
    
    # Initiate array and pull apps with an error status from EE2
    job_array = []
    filters = {'status': 'error', 'finished__gt': epoch_finish_begin, 'finished__lt': epoch_end}
    params = {'start_time': epoch_start_begin, 'end_time': epoch_end, 'filter': filters, 'ascending': 0,  "limit": 1000000}
    stats = ee2.check_jobs_date_range_for_all(params=params)
    # Iterate through 'errored' jobs/apps
    for errored in stats['jobs']:
        # Convert timestamps from milliseconds to seconds.
        millisec_crtime = errored["created"] / 1000.0
        # Format date to ISO and calender date
        creation_time_iso = datetime.datetime.utcfromtimestamp(millisec_crtime).isoformat()
        # Create basic struct of error dictionary
        errlog_dictionary = {"user": errored["user"], "error": '_NULL_',
                             'traceback': '_NULL_', 'name_of_error': '_NULL_',
                             'workspace_id': '_NULL_', "app_id": "_NULL_",
                             'type': 'ee2errorlogs', "job_id": errored["job_id"],
                             'timestamp': creation_time_iso, "err_prefix": "_NULL_",
                             'error_code': '_NULL_', 'obj_references': "_NULL_"}
        if "job_input" in errored.keys():
            if "app_id" in errored["job_input"].keys():
                errlog_dictionary["app_id"] = errored["job_input"]["app_id"].replace(".", "/")
        # Check if workspace ID is present in EE2 log for app
        if 'wsid' in errored.keys():
            # Send the error to helper functions for formatting
            filled_error_dictionary = check_keys_with_wsid.check_keys_with_wsid(errored, errlog_dictionary)
            error_msg = filled_error_dictionary['error']
            formatted_error_dictionary = filter.filter_error(error_msg, filled_error_dictionary)
            job_array.append(formatted_error_dictionary)
            c.to_logstash_json(formatted_error_dictionary)
        else:
            # Check if the errormsg key even exist in the log
            if 'errormsg' in errored.keys():
                error_msg = errlog_dictionary['error'] = errored['errormsg']
                errlog_dictionary['traceback'] = errored['errormsg']
                formatted_error_dictionary = filter.filter_error(error_msg, errlog_dictionary)
                # Job array can be printed at the end of the function for debugging as the array contains all the logs that were sent to Logstash
                job_array.append(formatted_error_dictionary)
                c.to_logstash_json(formatted_error_dictionary)
            else:
                errlog_dictionary['err_prefix'] = "_NULL_"
                errlog_dictionary['category'] = "_NULL_"
                job_array.append(errlog_dictionary)
                c.to_logstash_json(errlog_dictionary)
    print("{} Error logs added to Logstash for date range: {} to {}".format(len(job_array), start_date, end_date))
