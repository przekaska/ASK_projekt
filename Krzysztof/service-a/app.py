from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# service name from compose network
SERVICE_B_URL = os.environ.get("SERVICE_B_URL", "https://service-b-proxy/info")
CA_CERT = "/certs/ca.crt"

@app.route("/")
def root():
    try:
        r = requests.get(SERVICE_B_URL, timeout=2, verify=CA_CERT)
        r.raise_for_status()
        b = r.json()
    except Exception as e:
        return jsonify({"service": "A", "status": "error", "error": str(e)}), 502

    return jsonify({"service": "A", "status": "ok", "from_b": b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
