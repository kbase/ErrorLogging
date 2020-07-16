# KBase Error Logging

This repository contains code for gathering and uploading KBase app errors from user job
states in the catalog, workspace and execution engine. This repository is run through a cron job every night.
The main function in the repo is get_errored_apps_EE2. 
The cron job calls the upload_errorlogs function that calls the main get_errored_apps_EE2 function. 

## Getting Started
Before being able to run this docker container a ".env" file needs to be made. 
It should be called .env and should contain the following:

* USER_TOKEN=<TOKEN>
* SERVICE_WIZARD_URL=<URL>
* ELASTICSEARCH_HOST=<URL>

Please ask a fellow developer for the correct url paths and alter your .env 
file accordingly. 

The script in hooks/build is used to build a docker image named "kbase/errorlogging" 
from the current contents of the repo. You can simply run it by:
```sh
$ IMAGE_NAME=kbase/errorlogging hooks/build
```
Once it's built, one can run the source directory by the following command:
```sh
$ docker-compose run --rm ErrorLogging
```
Or one can run the error log cron job by:
```sh
$ docker-compose run --rm ErrorLogging ../bin/cron_shell.sh
```
If no dates are given the cron job imports error logs from the previous day. However,
if one wants to run the cron job over a specific date range one can simply 
run the following:
```sh
$ docker-compose run --rm ErrorLogging ../bin/cron_shell.sh MM-DD-YYYY MM-DD-YYYY
```
## Testing
To test the output of the main script (pull_app_stats) without uploading logs to
logstash, one should comment out the following export statement:
```sh
c.to_logstashJson(errlog_dictionary)
```
and one should return "error_logs"

