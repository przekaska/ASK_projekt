from flask import Flask, send_file, abort, request
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path("files").resolve()

@app.route("/")
def index():
    return "Hello from Docker HTTP server!\n"

@app.route("/health")
def health():
    return "OK\n"

@app.route("/file/<path:filepath>", methods=["GET"])
def get_file(filepath):
    target_path = (BASE_DIR / filepath).resolve()

    if not str(target_path).startswith(str(BASE_DIR)):
        abort(403)

    if not target_path.is_file():
        abort(403)

    return send_file(target_path, as_attachment=False)


@app.route("/file/<path:filepath>", methods=["POST"])
def create_file(filepath):
    target_path = (BASE_DIR / filepath).resolve()
    
    if not str(target_path).startswith(str(BASE_DIR)):
        abort(403)

    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "wb") as f:
        f.write(request.data)

    return f"Saved file: {filepath}\n", 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
