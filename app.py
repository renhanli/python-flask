from flask import Flask
import pyodbc
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 10/27"
