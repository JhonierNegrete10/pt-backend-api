# Use the official Python image
FROM python:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /app

# Update and install Ubuntu packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    git \
    curl \
    wget \
    iputils-ping \
    net-tools \
    && apt-get clean



# Copy requirements.txt and install Python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /app .
RUN pip install requests

CMD [ "python", "main.py"]

