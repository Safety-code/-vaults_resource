from flask import Flask
from datetime import datetime
import re
import app
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

# @app.route('/hello/')
# @app.route("/hello/<name>")
# def hello_there(name=None):
#     now = datetime.now()
#     formatted_now = now.strftime("%a, %d %b, %y at %X")
#     'Wednesday, 28 August, 2019 at 15:08:00'

@app.route('/hello/')
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


    #filter the name argument to letters only using regular expressions. URL arguments
    #can contain arbitrary text, so we restrict to safe characters only.

    match_object = re.match("a-zA-Z"+ name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, "+ clean_name + "! It's " + formatted_now
    return content
