#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn storefront.wsgi:application --bind 0.0.0.0:8000
