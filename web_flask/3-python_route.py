#!/usr/bin/python3
"""
Using flask to start a simple web server
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')#!/usr/bin/python3
