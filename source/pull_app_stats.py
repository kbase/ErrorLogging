from biokbase.service.Client import Client as ServiceClient
import os
import re
import ast
import pprint
import datetime
import client as c
import filter

token = os.environ['USER_TOKEN']
service_wizard_url = os.environ['SERVICE_WIZARD_URL']
yesterday = (datetime.date.today() - datetime.timedelta(days=1))
start_date_default = datetime.datetime.combine(yesterday, datetime.datetime.min.time())
end_date_default = datetime.datetime.combine(yesterday, datetime.datetime.max.time())

def get_app_stats(start_date=start_date_default, end_date=end_date_default):
    
    client = ServiceClient(service_wizard_url, use_url_lookup=True, token=token)
    
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
            
    metrics = client.sync_call('kb_Metrics.get_app_metrics', [{'epoch_range': [epoch_start,epoch_end]}])
    job_states = metrics[0]['job_states']
    # Initiate data structs and regaxPattern
    error_logs = []
    delimiters = "{", "}", "''", ":", ",", "message"
    regexPattern = '|'.join(map(re.escape, delimiters))
    # Iterate over job logs from call
    for log in job_states:
        # Convert timestamps from milliseconds to seconds.
        millisec_crtime = log["creation_time"]/1000.0
        # Format date to ISO and calender date
        creation_time_iso = datetime.datetime.utcfromtimestamp(millisec_crtime).isoformat()
        if log.get('error'):
            # Initiate dictionary
            errlog_dictionary = {"user": log["user"], "error_msg": "_NULL_",
                                 "app_id": "None", "type": "errorlogs",
                                "job_id": log["job_id"], 'timestamp': creation_time_iso,
                                 "err_prefix": "_NULL_", "category": "_NULL_"}
            if "app_id" in log:
                # get error log for app and skip 'queued' or 'in-progress' jobs
                error = log.get('status')
                non_errorstatuses = ["queued", "in-progress"]
                errlog_dictionary['app_id'] = log["app_id"]
                if error:
                    formatted_error_dictionary = filter.filter_error(error, errlog_dictionary, log)
                    error_logs.append(formatted_error_dictionary)
                    c.to_logstash_json(formatted_error_dictionary)
                else:
                    error_logs.append(errlog_dictionary)
                    c.to_logstash_json(errlog_dictionary)
            else:
                errlog_dictionary['app_id'] = 'None'
                error_logs.append(errlog_dictionary)
                c.to_logstash_json(errlog_dictionary)
                
                    
    print("{} Error logs added to Logstash for date range: {} to {}".format(len(error_logs), start_date, end_date))
