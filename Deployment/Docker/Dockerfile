# Adding the base image
FROM python:3.12-bullseye

# Setting the working directory
WORKDIR /app

# Copying the application files
COPY ./IrisProject/* .

# Installing the required packages
RUN pip install poetry 
    # && poetry config virtualenvs.create false \
    # && poetry install

# Run the application
CMD ["poetry", "run", "python", "run.py", "predict"]