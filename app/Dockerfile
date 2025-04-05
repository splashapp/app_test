FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
# Diese Zeile müsste angepasst werden:
# COPY app/app.py .
# Oder alternativ:
COPY ./app/* .
EXPOSE 5000
CMD ["python", "app.py"]