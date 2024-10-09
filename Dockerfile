# Pull official base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Run migrations and collect static files
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "collectstatic", "--noinput"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
