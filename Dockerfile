FROM python:3.9.5-alpine

COPY poetry.lock /
COPY pyproject.toml .
RUN pip install poetry && \
    poetry config settings.virtualenvs.create false && \
    poetry install

COPY . /

EXPOSE 8000

CMD gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0