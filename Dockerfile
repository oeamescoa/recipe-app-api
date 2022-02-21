FROM python:3.7-alpine
LABEL maintainer="Oscar Amezcua"

# set environment variable
ENV PYTHONUNBUFFERED 1

# copy and run requirements from local directory onto Docker image
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# create our app directory, move into it, and copy all local /app files onto Docker image
RUN mkdir /app
WORKDIR /app
copy ./app /app

# move from root user to user user (if someone compromises application they have access to root)
RUN adduser -D user
USER user

