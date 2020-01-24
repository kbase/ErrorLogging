

from biokbase.service.Client import Client as ServiceClient
import os
import re
import ast
import pprint
import datetime
import client as c
import error_categories

token = os.environ['USER_TOKEN']
service_wizard_url = os.environ['SERVICE_WIZARD_URL']
yesterday = (datetime.date.today() - datetime.timedelta(days=1))
start_date_default = datetime.datetime.combine(yesterday, datetime.datetime.min.time())
end_date_default = datetime.datetime.combine(yesterday, datetime.datetime.max.time())


def get_app_stats(start_date=start_date_default, end_date=end_date_default):

    client = ServiceClient(service_wizard_url, use_url_lookup=True, token=token)

    if type(start_date) == str:
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

    metrics = client.sync_call('kb_Metrics.get_app_metrics',
                               [{'epoch_range': [epoch_start, epoch_end]}])
    job_states = metrics[0]['job_states']
    error_logs = []
    delimiters = "{", "}", "''", ":", ",", "2", "message"
    regexPattern = '|'.join(map(re.escape, delimiters))
    for log in job_states:
        # Convert timestamps from milliseconds to seconds.
        millisec_crtime = log["creation_time"]/1000.0
        creation_time_iso = datetime.datetime.utcfromtimestamp(millisec_crtime).isoformat()
        if log.get('error'):
            if "app_id" in log:
                error = log.get('status')
                non_errorstatuses = ["queued", "in-progress"]
                if error is None:
                    errlog_dictionary = {"user": log["user"], "error_msg": str(error), "app_id":
                                         "None", "type": "errorlogs", "job_id": log["job_id"],
                                         'timestamp': creation_time_iso,
                                         "err_prefix": "_NULL_", "category": str(error)}

                    error_logs.append(errlog_dictionary)
                    c.to_logstashJson(errlog_dictionary)
                elif ' ' in error:
                    # Pull error statement out of tuple as 'prefix'
                    # Else go through standard error cleaning procedure
                    if 'No such file or directory' in error:
                        error_clean=re.sub( r'([\"{}\\><])', '', error).replace("''", '').strip() 
                        error_tuple = ast.literal_eval(error_clean)
                        prefix_clean = error_tuple[1]
                    else:
                        error_clean=re.sub( r'([\'"{}\\><])', '', error).replace("''", '').strip()
                        prefix = re.split(regexPattern, error)
                        prefix = list(filter(lambda s:any([c.isalnum() for c in s]), prefix))[0]
                        prefix_clean = re.sub( r'([\'"{}\\><])', '', prefix).replace("(", ' ').replace("[", '').strip()
                    # Get error category and place in error log
                    category = error_categories.add_category(log)
                    errlog_dictionary = {"user": log["user"], "error_msg": error_clean,
                                         "app_id": log["app_id"], "type": "errorlogs",
                                         "job_id": log["job_id"], 'timestamp': creation_time_iso,
                                         "err_prefix": prefix_clean, "category": category}
                    error_logs.append(errlog_dictionary)
                    c.to_logstashJson(errlog_dictionary)
                elif '' in error:
                    error.strip()
                    if len(error) == 2 or error == "'()'":
                        errlog_dictionary = {"user" : log["user"], "error_msg": "_NULL_", 
                                             "app_id" : log["app_id"], "type": "errorlogs",
                                             "job_id": log["job_id"], 'timestamp': creation_time_iso, 
                                             "err_prefix": "_NULL_", "category":"_NULL"}
                        error_logs.append(errlog_dictionary)
                        c.to_logstashJson(errlog_dictionary)
                    elif not error:
                        errlog_dictionary = {"user" : log["user"], "error_msg": "_NULL_", 
                                             "app_id" : log["app_id"], "type": "errorlogs",
                                             "job_id": log["job_id"], 'timestamp': creation_time_iso, 
                                             "err_prefix": "_NULL_", "category": "_NULL_"}
                        error_logs.append(errlog_dictionary)
                        c.to_logstashJson(errlog_dictionary)
                    elif any(element in error for element in non_errorstatuses):
                        continue
                    else:
                        prefix = re.split(regexPattern, error)
                        prefix = list(filter(lambda s:any([c.isalnum() for c in s]), prefix))[0]
                        prefix_clean = re.sub( r'([\'"{}\\><])', '', prefix).replace("(", ' ').replace("[", '').strip()
                        error_clean=re.sub( r'([\'"{}\\><])', '', error).replace("''", '').strip()
                        category = error_categories.add_category(log)
                        errlog_dictionary = {"user" : log["user"], "error_msg": error_clean, 
                                             "app_id" : log["app_id"], "type": "errorlogs",
                                             "job_id": log["job_id"], 'timestamp': creation_time_iso, 
                                             "err_prefix": prefix_clean, "category": category}
                        error_logs.append(errlog_dictionary)
                        c.to_logstashJson(errlog_dictionary)
            else:
                error = log.get('status')
                errlog_dictionary = {"user" : log["user"], "error_msg": str(error), 
                                     "app_id" : "None", "type": "errorlogs",
                                     "job_id": log["job_id"], 'timestamp': creation_time_iso,
                                     "err_prefix": "_NULL_", "category": str(error)}
                error_logs.append(errlog_dictionary)
                c.to_logstashJson(errlog_dictionary)

    print("{} Error logs added to Logstash for date range: {} to {}".format(len(error_logs), start_date, end_date))
