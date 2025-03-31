
# Build the Docker image
docker build -t ingram-scanner .

# Run a simple scan with default settings
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output ingram-scanner -i /app/input/targets -o /app/output

# Run with specific ports
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output ingram-scanner -i /app/input/targets -o /app/output -p 80 443 8080

# Run with increased concurrency
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output ingram-scanner -i /app/input/targets -o /app/output -t 1000

# Run with Docker Compose (simplest option)
docker-compose up