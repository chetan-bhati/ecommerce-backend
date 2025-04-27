# Use the official Python 3.12 image from Docker Hub as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to access the app
EXPOSE 8000

# Set the environment variable to avoid creating .pyc files and enable debugging
ENV PYTHONUNBUFFERED 1

# Run the Django app with the default command (usually `python manage.py runserver`)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
