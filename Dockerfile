# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app/ app/

# Expose port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]
