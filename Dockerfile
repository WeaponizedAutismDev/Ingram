FROM python:3.10-slim

WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    nmap \
    curl \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directories with proper permissions
RUN mkdir -p /app/input /app/output/snapshots /app/data && \
    chmod -R 775 /app && \
    chmod -R 775 /app/input && \
    chmod -R 775 /app/output && \
    chmod -R 775 /app/output/snapshots && \
    chmod -R 775 /app/data

# Default command (can be overridden)
ENTRYPOINT ["python3", "run_ingram.py"]
CMD ["-h"]