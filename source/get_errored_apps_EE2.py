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
    if isinstance(start_date, str):
        # Format date strings to datetime objects
        start_date_dt = datetime.datetime.strptime(start_date, '%m-%d-%Y')
        start_date_min = datetime.datetime.combine(start_date_dt, datetime.datetime.min.time())
        end_date_dt = datetime.datetime.strptime(end_date, '%m-%d-%Y')
        end_date_max = datetime.datetime.combine(end_date_dt, datetime.datetime.max.time())

        # datetime to epoch. Epoch format needed for elastic query
        epoch_start = int(start_date_min.strftime('%s')) * 1000
        epoch_end = int(end_date_max.strftime('%s')) * 1000
    else:
        # datetime to epoch. Epoch format needed for elastic query
        epoch_start = int(start_date.strftime('%s')) * 1000
        epoch_end = int(end_date.strftime('%s')) * 1000
    job_array = []
    params = {'start_time': epoch_start, 'end_time': epoch_end, 'filter': ['status=error'], 'ascending': 0}
    stats = ee2.check_jobs_date_range_for_all(params=params)
    for errored in stats['jobs']:
        # Convert timestamps from milliseconds to seconds.
        millisec_crtime = errored["created"] / 1000.0
        # Format date to ISO and calender date
        creation_time_iso = datetime.datetime.utcfromtimestamp(millisec_crtime).isoformat()
        errlog_dictionary = {"user": errored["user"], "error": '_NULL_',
                             'traceback': '_NULL_', 'name_of_error': '_NULL_',
                             'workspace_id': '_NULL_', "app_id": "_NULL_",
                             'type': 'ee2errorlogs', "job_id": errored["job_id"],
                             'timestamp': creation_time_iso, "err_prefix": "_NULL_",
                             'error_code': '_NULL_', 'obj_references': "_NULL_"}
        if 'wsid' in errored.keys():
            filled_error_dictionary = check_keys_with_wsid.check_keys_with_wsid(errored, errlog_dictionary)
            error_msg = filled_error_dictionary['error']
            formatted_error_dictionary = filter.filter_error(error_msg, filled_error_dictionary)
            job_array.append(formatted_error_dictionary)
            c.to_logstash_json(errlog_dictionary)
        else:
            if 'errormsg' in errored.keys():
                error_msg = errlog_dictionary['error'] = errored['errormsg']
                errlog_dictionary['traceback'] = errored['errormsg']
                formatted_error_dictionary = filter.filter_error(error_msg, errlog_dictionary)
                job_array.append(formatted_error_dictionary)
                c.to_logstash_json(errlog_dictionary)
            else:
                errlog_dictionary['err_prefix'] = "_NULL_"
                errlog_dictionary['category'] = "_NULL_"
                job_array.append(errlog_dictionary)
                c.to_logstash_json(errlog_dictionary)
    print("{} Error logs added to Logstash for date range: {} to {}".format(len(job_array), start_date, end_date))
    
