FROM python:3.10-slim

# -----------------------------
# Install system dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    nodejs npm curl unzip openjdk-11-jdk \
    && apt-get clean

# -----------------------------
# Install Appium 2 + drivers
# -----------------------------
RUN npm install -g appium@2.11.0 \
    && appium driver install uiautomator2

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

