#!/bin/sh

until cd /app/task
do
  echo "Waiting for server volume..."
done

until ./manage.py migrate
do
  echo "Waiting for db to be ready..."
  sleep 2
done

./manage.py collectstatic --noimput

gunicorn task.wsgi --bind 0.0.0.0:8000 --workers 3 --threads 3