# Verwende ein leichtgewichtiges Python-Basis-Image
FROM python:3.10-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Flask installieren (keine separate requirements.txt nötig)
RUN pip install --no-cache-dir flask

# Anwendungscode kopieren
COPY app.py .

# Port freigeben
EXPOSE 5000

# Startbefehl definieren
CMD ["python", "app.py"]
