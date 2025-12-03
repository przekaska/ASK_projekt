FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py .
COPY files ./files

EXPOSE 8080

CMD ["python", "app.py"]
