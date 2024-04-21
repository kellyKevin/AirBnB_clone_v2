#!/usr/bin/python3
"""Module - script that starts a Flask web application"""
from flask import Flask
app = Flask(_name_)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles the root url"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handles hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Handles /c/<text> route"""
    return 'C {}'.format(text.replace('_', ' '))


if _name_ == '_main_':
    app.run("0.0.0.0", 5000)
