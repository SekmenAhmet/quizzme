from flask import Flask
from config import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/api/quiz-info")
def quizInfo():
    return {"message": "test"}

if "__main__" == __name__:
    app.run(host="0.0.0.0", port=config["PORT"])
