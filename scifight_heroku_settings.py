import os
import sys
import logging
import dj_database_url

# noinspection PyUnresolvedReferences
from scifight_proj.settings import *

DEBUG            = False
WSGI_APPLICATION = 'scifight_heroku_wsgi.application'
SECRET_KEY       = os.environ['SCIFIGHT_SECRET_KEY']
ALLOWED_HOSTS    = [x.strip() for x in os.environ['SCIFIGHT_ALLOWED_HOSTS'].split(",")]
DATABASES        = {'default': dj_database_url.config()}

logging.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# '
           '%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.DEBUG,
    stream=sys.stdout)
