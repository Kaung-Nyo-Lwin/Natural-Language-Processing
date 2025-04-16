# Use Python 3.10.12 image as base
FROM python:3.10.12

# Set working directory
WORKDIR /root/app

# Copy requirements.txt
COPY app/requirements.txt .

# Install system dependencies needed for torch
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./root/app/


# Command to run the application
CMD ["python3", "main.py"]
