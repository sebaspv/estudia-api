# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get -y update && apt-get -y install git && apt-get -y install wget && pip3 install -r requirements.txt
RUN python -m nltk.downloader universal_tagset && python -m nltk.downloader stopwords && python -m spacy download en && wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz && tar -xvf  s2v_reddit_2015_md.tar.gz

COPY . .

CMD [ "python3", "main.py"]