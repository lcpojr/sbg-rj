FROM python:3.7.3
LABEL maintainer="Luiz Carlos"

RUN mkdir /app
WORKDIR /app

# Env vars
ENV PYTHONUNBUFFERED 1

# Installing dependencies
RUN apt-get update && apt-get upgrade -y
RUN pip install -U pip setuptools
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD . /app/

# Django service
EXPOSE 8000