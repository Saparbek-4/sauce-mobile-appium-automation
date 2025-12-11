FROM python:3.10-slim

# -----------------------------
# Install system dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    curl unzip default-jdk \
    && apt-get clean

# -----------------------------
# App working directory
# -----------------------------
WORKDIR /app

# Copy project
COPY . /app

# -----------------------------
# Install Python dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Default test run command
# -----------------------------
CMD ["bash", "run_tests.sh"]

