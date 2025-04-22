# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Install OS dependencies (optional: if you want git or build tools)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy app source code
COPY ./app ./app

# Set environment variable for PYTHONPATH
ENV PYTHONPATH=/app



# Set default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]