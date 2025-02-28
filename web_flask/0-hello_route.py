#!/usr/bin/python3
"""Starts flask web aplication"""
from flask import Flask, request


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a Hello message."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
