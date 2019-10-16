
from biokbase.service.Client import Client as ServiceClient
import os
import datetime
import json
import client as c

token = os.environ['USER_TOKEN']
service_wizard_url = os.environ['SERVICE_WIZARD_URL']

def get_app_stats(start_date, end_date):

    client = ServiceClient(service_wizard_url, use_url_lookup=True, token=token)

    if type(start_date) == str:
        # Format date strings to datetime objects
        start_date = datetime.datetime.strptime(start_date, '%m-%d-%Y')
        start_date = datetime.datetime.combine(start_date, datetime.datetime.min.time())
        end_date = datetime.datetime.strptime(end_date, '%m-%d-%Y')
        end_date = datetime.datetime.combine(end_date, datetime.datetime.max.time())

        # datetime to epoch. Epoch format needed for elastic query
        epoch_start = int(start_date.strftime('%s')) * 1000
        epoch_end = int(end_date.strftime('%s')) * 1000
    else:
        # datetime to epoch. Epoch format needed for elastic query
        epoch_start = int(start_date.strftime('%s')) * 1000
        epoch_end = int(end_date.strftime('%s')) * 1000

    metrics = client.sync_call('kb_Metrics.get_app_metrics', [{'epoch_range': [epoch_start, epoch_end]}])
    job_states = metrics[0]['job_states']

    error_logs = []
    for log in job_states:
        if log.get('error'):
            errlog_dictionary = {"user": log["user"], "error_msg": log.get('status'), "app_id": log["app_id"],
                                 "job_id": log["job_id"], "type": "joblogs"}
            c.to_logstashJson(errlog_dictionary)
            error_logs.append(errlog_dictionary)

    #with open(os.path.join('../JobLogs', 'error_logs.json'), 'w') as fout:
        #json.dump(error_logs, fout)

    return error_logs
















































