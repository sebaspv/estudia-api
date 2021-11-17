# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader universal_tagset
RUN python -m spacy download en
RUN wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
RUN tar -xvf  s2v_reddit_2015_md.tar.gz

COPY . .

CMD [ "python3", "main.py"]