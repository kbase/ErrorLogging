# UploadErrorLogs
#
import pull_app_stats
import time
import datetime
print("############################################")
print("App Stats Upload (UTC): " + str(datetime.datetime.utcnow()))
start_time = time.time()
#start_date = "01-10-2019""
#end_date = "31-10-2019"
#pull_app_stats.get_app_stats(start_date,end_date)
pull_app_stats.get_app_stats()
print("Uploading error logs to logstash stats took ", time.time() - start_time, " seconds to run")
