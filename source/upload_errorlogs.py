# UploadErrorLogs
#
import pull_app_stats
import time
import sys
import datetime
print("############################################")
print("App Stats Upload (UTC): " + str(datetime.datetime.utcnow()))
start_time = time.time()

if len(sys.argv) == 2:
    start_date = sys.argv[0]
    end_date = sys.argv[1]

    try:
        datetime.datetime.strptime(start_date, '%m-%d-%Y')
    except ValueError:
        raise ValueError("Incorrect start data format, should be MM-DD-YYYY")

    try:
        datetime.datetime.strptime(end_date, '%m-%d-%Y')
    except ValueError:
        raise ValueError("Incorrect end data format, should be MM-DD-YYYY")
    pull_app_stats.get_app_stats(start_date, end_date)
    print("Uploading error logs to logstash stats took ",
          time.time() - start_time, " seconds to run")

elif len(sys.argv) == 0:
    pull_app_stats.get_app_stats()
    print("Uploading error logs to logstash stats took ",
          time.time() - start_time, " seconds to run")

else:
    print("Invalid number of arguments given")
