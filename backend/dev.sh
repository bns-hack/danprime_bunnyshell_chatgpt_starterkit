#!/bin/sh
#Runs python server in the background with auto-reload
#FOR DEV PURPOSES ONLY
#
/usr/local/bin/python /usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --reload-dir /code/app
