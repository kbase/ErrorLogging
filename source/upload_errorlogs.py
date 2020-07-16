# UploadErrorLogs
# This Function is the main uploader function that the cron job run. It can dates as system arguments (sys.argv)
# The first sys.argv is the function called the 2nd and 3rd are the start and end dates respectively
# If sys.argv is just the function then it runs for yesterday
import get_errored_apps_EE2
import time
import sys
import datetime
print("############################################")
print("App Stats Upload (UTC): " + str(datetime.datetime.utcnow()))
start_time = time.time()

if len(sys.argv) == 3:
    start_date = sys.argv[1]
    end_date = sys.argv[2]

    try:
        datetime.datetime.strptime(start_date, '%m-%d-%Y')
    except ValueError:
        raise ValueError("Incorrect start data format, should be MM-DD-YYYY")

    try:
        datetime.datetime.strptime(end_date, '%m-%d-%Y')
    except ValueError:
        raise ValueError("Incorrect end data format, should be MM-DD-YYYY")

    get_errored_apps_EE2.get_errored_apps(start_date, end_date)
    print("Uploading error logs to logstash stats took ",
          time.time() - start_time, " seconds to run")

elif len(sys.argv) == 1:
    get_errored_apps_EE2.get_errored_apps()
    print("Uploading error logs to logstash stats took ",
          time.time() - start_time, " seconds to run")

else:
    print("Invalid number of arguments given")
