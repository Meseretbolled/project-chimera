# Project Chimera — Agent Infrastructure Container

FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install pip dependencies
RUN pip install --upgrade pip
# Ensure build tooling is available and install project + test deps
RUN pip install --upgrade pip setuptools wheel --no-cache-dir

# Install the package in editable mode
RUN pip install -e . --no-cache-dir

# Install test runner (keep dev/test deps explicit)
RUN pip install pytest --no-cache-dir

# Default command: run test suite
CMD ["pytest", "-v"]
