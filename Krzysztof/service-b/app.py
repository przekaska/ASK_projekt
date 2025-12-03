from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/info")
def info():
    return jsonify({"service": "B", "status": "ok"})

if __name__ == "__main__":
    # Bind to 0.0.0.0 so container exposes it
    app.run(host="0.0.0.0", port=5000)
