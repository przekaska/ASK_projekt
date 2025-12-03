FROM python:3.12-slim

ENV SERVER_URL=http://server:8080

COPY workspace workspace
RUN chmod +x /workspace/send_file.sh /workspace/receive_file.sh

WORKDIR /workspace
CMD ["/bin/sh"]

