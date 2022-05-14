#!/usr/bin/python3
"""
    Script to init flask application
"""

from flask import Flask, render_template


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

@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """
        Url serving simple text with variable
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>)', strict_slashes=False)
def pythonIsCool(text='is cool'):
    """
        Url serving simple text with variable
    """
    return 'Python' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def isInteger(n):
    """
        Url serving check if n is integer
    """
    return '{:d} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def ifIntRender(n):
    """
        Url serving check if n is integer
        and if true, render template
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
