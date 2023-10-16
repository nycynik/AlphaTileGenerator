FROM python:3.12
# python image from docker hub https://hub.docker.com/_/python

## Java

# Install Java
RUN apt update && apt install -y sudo && sudo apt install default-jdk -y

## Python & Dependencies

# Upgrade pip
RUN pip install --upgrade pip

# Install production dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Install development dependencies
COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install -r /tmp/requirements-dev.txt && rm /tmp/requirements-dev.txt

