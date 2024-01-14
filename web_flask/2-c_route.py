#!/usr/bin/python3
"""Import the aplications"""
from flask import Flask
from markupsafe import escape

"""Calls the app"""
app Flask = (__name__)

@app.route(/, strict_slashes=False)
def hello_hbnb():
    """Shows the welcome message"""
    return 'Hello HBNB!'

@app.route(/hbnb, strict_slashes=False)
def hbnb():
    """Shows holbies"""
    return 'HBNB'

@app.route(/c/<text>, strict_slashes=False)
def c_text():
    """Shows C with the input text"""
    return f'C {escape(text.replace("_", " "))}'


if __name__ == '__main__':
    """Host and port running"""
    app.run(host='0.0.0.0', port=5000)