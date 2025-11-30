FROM python:3.12-slim
WORKDIR /app

RUN pip install websockets

ENV PYTHONUNBUFFERED=1
COPY client.py /app/client.py

CMD ["python", "client.py"]
