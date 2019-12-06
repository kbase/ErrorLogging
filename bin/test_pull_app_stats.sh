#!/bin/bash                                                                                                                           
python error_categories.py

python test_pull_app_stats.py

python test_upload_errorlogs.py $*
