from .base import *

ALLOWED_HOSTS=['3.38.245.208']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '39-10qjswl',
        'HOST': 'ls-94339b862e8c4480cd0751df7167f95484c94900.czefhdta4k4x.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
