# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

copy paralelism.py paralelism.py

CMD ["python3", "paralelism.py"]

#https://docs.docker.com/language/python/build-images/