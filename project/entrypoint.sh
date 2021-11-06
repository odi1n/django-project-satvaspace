#!/usr/bin/env bash

python manage.py migrate --noinput
python manage.py createsuperuser --noinput --username admin --email admin@admin.ru --password Qweqwe123.

exec "$@"
