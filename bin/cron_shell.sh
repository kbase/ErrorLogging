#!/bin/bash

python error_categories.py

python pull_app_stats.py

python upload_errorlogs.py $*
