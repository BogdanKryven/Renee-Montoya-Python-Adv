FROM python:latest

MAINTAINER Bohdan Kryven 'bodyan1108@gmail.com'

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py



#FROM ubuntu:20.04
#
#MAINTAINER Bohdan Kryven 'bodyan1108@gmail.com'
#
#WORKDIR app
#
#COPY . /app
#
#RUN apt-get update -y
#RUN apt-get install -y python3-pip python3
#RUN pip install -r requirements.txt
#
#ENTRYPOINT ["python3"]
#
#CMD ["app.py"]
