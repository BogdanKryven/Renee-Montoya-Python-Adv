FROM python:latest

MAINTAINER Bohdan Kryven 'bodyan1108@gmail.com'

WORKDIR /application

COPY ./app /application

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=8080
