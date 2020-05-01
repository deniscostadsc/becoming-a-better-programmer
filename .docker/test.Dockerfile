FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

RUN pip install -U pip

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
