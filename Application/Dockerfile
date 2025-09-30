# Use Python 3.11 slim image
FROM python:3.11-slim

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set port for Fly.io
ENV PORT=8080
EXPOSE 8080

# Start app with gunicorn
CMD ["gunicorn", "flaskapp:app", "-b", "0.0.0.0:8080"]
