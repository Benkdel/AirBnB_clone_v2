#!/usr/bin/python3
"""
    Script to init flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
        Url serving simple text
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Url serving simple text
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
