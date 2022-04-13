#!/bin/sh

# wait for Postgres instance being up and healthy
echo "Waiting for mongo..."

# loop runs until something like
# "Connection to web-db port 5432 [tcp/postgresql] succeeded!" is returned
while ! nc -z mongo 27017; do
  sleep 0.1
done

echo "MongoDB started"

# shellcheck disable=SC2093
exec gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0

exec "$@"