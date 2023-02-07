# Use a lightweight base image
FROM python:3.9-alpine as base

# Set the working directory
WORKDIR /app

# Copy the application files
COPY requirements.txt .
COPY main.py .

# Install the required packages
RUN apk add --no-cache --virtual .build-deps build-base && \
    pip install -r requirements.txt && \
    apk del .build-deps

# Set the environment variable
ENV FLASK_APP=main.py

# Expose the port for the Flask application
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]