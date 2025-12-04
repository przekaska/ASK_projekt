FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        net-tools \
        iputils-ping \
        iproute2 \
        tcpdump \
        curl \
        procps \
        nmap \ 
        dsniff

ENV SERVER_URL=http://server:8080

COPY workspace workspace
RUN chmod +x workspace/*.sh

WORKDIR /workspace
CMD ["/bin/sh"]

