#!/usr/bin/python3
"""
    Testing a simple web_flask application
"""

from flask import Flask, render_template, url_for
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('welcome.html', name=name)

@app.route('/<username>')
def say_hello(username):
    userName = escape(username)
    return render_template('sayHello.html', name=userName)

