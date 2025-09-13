# Using the official Python image
FROM python:3.12-slim

# Install the working directory
WORKDIR /app

# Copy the dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Creating a non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Opening the port
EXPOSE 5000

# Launching the app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]