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
## Testing with Logstash
To test the output of the cron job or main script (get_errored_apps_EE2) through Logstash, one must set up a 'Logstash Listener/Debugger'.
First fork then pull the Logstash repo (https://github.com/kbase/logstash) into a separate directory on docker03, construct a docker-compose.yml and env file containing the following:
```sh
IMAGE_NAME=
DOCKER_REPO=
``` 
then run:
```sh
docker run --rm -it -e debug_output=True -p 9000:9000 -p 5044:5044 kbase/logstash
```
If port 9000 is taken, run the following Docker commands to find the container name running on 9000:
```sh
docker ps | grep 9000
```
then 
```sh
docker kill CONATAINER_NAME
```
Once the Logstash Listener/Debugger is up and running, you need to change the ELASTICSEARCH_HOST url to 172.****** (ask Steve Chan for the url) 
in your .env for your System Metrics environment. Now run the System Metrics cron job described above and view 
its output in the Logstash Debugger. 

## Testing
To test the output of the main script (get_errored_apps_EE2) without uploading logs to
logstash, one should comment out the following export statement:
```sh
c.to_logstashJson(errlog_dictionary)
```
and one should return "job_array"

