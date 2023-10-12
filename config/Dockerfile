FROM python:3.9.17-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt