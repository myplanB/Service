#!/bin/bash

nohup gunicorn -w 2 Service.wsgi -b 0.0.0.0:8000 > /tmp/gunicon.log 2>&1 &
