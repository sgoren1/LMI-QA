#!/bin/sh
cd /home/yizhu/Wiki_QA_System-master/mysite/
gunicorn -c gunicorn.Conf.py mysite.wsgi