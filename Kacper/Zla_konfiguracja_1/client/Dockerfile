FROM alpine:3.20

RUN apk add --no-cache curl iputils-ping

ENV SERVER_URL=http://server:8080

COPY workspace workspace
RUN chmod +x /workspace/*.sh

WORKDIR /workspace
CMD ["/bin/sh", "inf_receive_file.sh"]

