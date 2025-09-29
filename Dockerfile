# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set port for Fly
ENV PORT=8080
EXPOSE 8080

# Start app with gunicorn
CMD ["gunicorn", "flaskapp:app", "-b", "0.0.0.0:8080"]
