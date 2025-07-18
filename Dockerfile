FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# COPY .env .

RUN useradd -m myuser && chown -R myuser /app
USER myuser

# Usa el script de inicio como comando
CMD alembic upgrade head && exec uvicorn app.main:app --host 0.0.0.0 --port 8000
