# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


# FROM python:3.8-slim-buster


# COPY . /flask-library
# WORKDIR /flask-library

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# # CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


# # FROM python:alpine3.7
# # COPY . /app
# # WORKDIR /app
# # RUN pip install -r requirements.txt
# # EXPOSE 5000
# CMD ["python3", "microservice.py" ]

