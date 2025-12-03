cd certs

# 1 — Tworzymy klucz CA
openssl genrsa -out ca.key 4096

# 2 — Tworzymy certyfikat CA
openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 \
  -subj "/CN=MyDockerCA" \
  -out ca.crt

# 3 — Klucz serwera B
openssl genrsa -out service-b.key 2048

# 4 — CSR
openssl req -new -key service-b.key \
  -subj "/CN=service-b" \
  -out service-b.csr

# 5 — Cert serwera podpisany przez CA
openssl x509 -req -in service-b.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out service-b.crt -days 365 -sha256
