# Use an official Python runtime as a parent image
FROM python:2.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Add requirments file
ADD requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
ADD . /code
