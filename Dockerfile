FROM python:3.8

WORKDIR /usr/src

COPY /apps/requirements.txt ./
COPY /apps/.env ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt