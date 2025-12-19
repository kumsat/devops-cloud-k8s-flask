FROM python:3.13-slim

# Create a non-root user (good security practice)
RUN useradd -m appuser

WORKDIR /app

# Copy only dependency files first (better caching)
COPY pyproject.toml README.md ./
COPY app/requirements.txt ./app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r app/requirements.txt

# Copy application source
COPY app/src ./app/src

# Run as non-root
USER appuser

# Flask runs on 5007 in your project
EXPOSE 5007

# Start the app
CMD ["python", "app/src/main.py"]

