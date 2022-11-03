#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
cp -R /home/password/web/static/* /home/password/web/staticfiles

exec "$@"