
import biokbase.narrative.clients as clients
from time import time
import datetime
import json

def get_app_stats(start_date, end_date):

    client = clients.get("service")

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

    with open('data3.json', 'w') as fout:
        json.dump(job_states, fout)

    return job_states

















































