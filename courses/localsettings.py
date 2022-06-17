import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '+y8scinypcm&-&p45&un6!jyz$_o5tp53+=*q_b%(0nd2optr)'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#STATIC_DIR = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [STATIC_DIR]

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]