#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

docker compose exec django_app python manage.py makemigrations --noinput
docker compose exec django_app python manage.py migrate --noinput

gunicorn storefront.wsgi:application --bind 0.0.0.0:8000
