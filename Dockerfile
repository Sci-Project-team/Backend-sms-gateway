FROM python:3.9-slim

WORKDIR /app

# Configure PYTHONPATH pour les imports relatifs
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie toute l'arborescence (y compris le dossier app/)
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
