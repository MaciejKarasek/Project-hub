FROM python:3.11.7
# baseimage Python 3.11.7
# https://hub.docker.com/_/python

# Copies all files into container /app/ folder
COPY . /app/

# Working directory
WORKDIR /app

# RUN - executing commands
RUN pip install -r requirements.txt

# Last command in Dockerfile that starts the app
CMD python app.py