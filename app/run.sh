#!/bin/sh

exec gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0