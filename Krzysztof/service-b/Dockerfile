# stage: build
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# stage: runtime (smaller)
FROM python:3.11-slim
# create non-root user
RUN useradd -m -u 1000 appuser
WORKDIR /app
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY app.py .
# drop file-system write permission for most layers; runtime needs /tmp maybe
RUN chmod -R 755 /app
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
