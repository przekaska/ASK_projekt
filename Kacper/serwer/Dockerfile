FROM python:3.12-slim
WORKDIR /app

RUN pip install websockets

ENV PYTHONUNBUFFERED=1

COPY serwer.py /app/serwer.py

EXPOSE 8765

CMD ["python", "serwer.py"]
