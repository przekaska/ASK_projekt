FROM alpine:3.20

RUN apk add --no-cache curl

ENV SERVER_URL=http://server:8080

COPY workspace workspace
RUN chmod +x /workspace/send_file.sh /workspace/receive_file.sh

WORKDIR /workspace
CMD ["/bin/sh"]

