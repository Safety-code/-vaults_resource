from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return "Drink more coffee"

app.run(host="0.0.0.0", port=8080)
