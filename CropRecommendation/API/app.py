import json
from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def home():
    return json.dumps({"status": "OK"}), {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run(debug=True)
