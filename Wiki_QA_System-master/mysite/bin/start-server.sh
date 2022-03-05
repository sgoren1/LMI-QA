#!/bin/sh
cd /home/LMI_NLP/Wiki_QA_System-master/mysite/
echo "i'am in wiki mysite"
source env/bin/activate
# cd mysite
echo "i'am in wiki mysite mysite if cd mysite"
gunicorn -c gunicorn.Conf.py mysite.wsgi