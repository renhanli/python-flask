from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    print(requests.__version__)
    return "Hello, World!"
