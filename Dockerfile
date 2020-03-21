# Docker file for Poplesia website
FROM ubuntu

MAINTAINER Pimin Konstantin Kefaloukos "skipperkongen@gmail.com"

RUN apt-get update -y --fix-missing
RUN apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY poplesia poplesia

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV FLASK_APP app.py

WORKDIR poplesia

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]
