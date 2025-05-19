# Add the base image
FROM python:3.12.10-bullseye

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry install


