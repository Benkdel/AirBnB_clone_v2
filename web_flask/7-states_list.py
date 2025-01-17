#!/usr/bin/python3
"""
    Script to init flask application
"""

from models.state import State
from models import storage
import sys
from flask import Flask, render_template

sys.path.append('../')


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def displayStatesList():
    """
        Url serving DB data
    """
    query_result = storage.all(State)
    states = []
    for key, val in query_result.items():
        states.append(val)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
