from .base import *

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default='*')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str("POSTGRES_DB"),
        'USER': env.str("POSTGRES_USER"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str("POSTGRES_HOST"),
        'POSTGRES_PORT': env.str("POSTGRES_PORT"),
    }
}