# Use a lightweight base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install the required packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable
ENV FLASK_APP=main.py

# Expose the port for the Flask application
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]