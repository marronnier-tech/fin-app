FROM python:3.10.1-bullseye

WORKDIR /opt/app

RUN pip install --upgrade pip
RUN pip install Flask gunicorn sqlalchemy

COPY requirements.txt .
