apt update && apt install -y docker.io
docker ps
docker run -it -v /:/host alpine sh
cd /host/mnt/host