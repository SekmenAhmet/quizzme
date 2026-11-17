from flask import Flask
from config import config

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


if "__main__" == __name__:
    app.run(host="0.0.0.0", port=config["PORT"])
