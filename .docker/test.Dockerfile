FROM python:3.8.3

ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip pip-tools

RUN mkdir /code
WORKDIR /code

COPY requirements/test.lock /code/
RUN pip install -r test.lock
