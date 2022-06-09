#!/bin/sh
echo "*** Running migrations ***"
python manage.py migrate

echo "*** starting dev server ***"
python manage.py runserver 0.0.0.0:8000