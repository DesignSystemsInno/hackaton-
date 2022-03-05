FROM python:3.9-slim
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app/