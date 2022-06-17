import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '+1Gsadhy%#@$gsad62hj3(zalupa)%&-&p45&un6!jyz$_o5tp53+=*q_b%(0nd2optr)'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "192.168.8.111"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main',
        'USER': 'userdb',
        'PASSWORD': 'devPASS',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#STATICFILES_DIRS = [
 #   BASE_DIR / "static"
# ]

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

#STATIC_DIR = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS =[STATIC_DIR]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]