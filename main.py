import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Dockerized Flask app! 🚀"


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("FLASK_RUN_HOST", "0.0.0.0"),
        port=int(os.environ.get("FLASK_RUN_PORT", 8080)),
        debug=False
    )
