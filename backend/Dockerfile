# backend/Dockerfile
FROM python:3.9-slim

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]
