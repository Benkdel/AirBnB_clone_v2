#!/usr/bin/python3
"""
    Script to init flask application
"""

import sys
from models.state import State
from models import storage
from flask import Flask, render_template


sys.path.append('../')

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def displayListOfStates():
    """
        Url serving DB data
    """
    query_result = storage.all(State)
    states = []
    for key, val in query_result.items():
        states.append(val)

    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def displayStateLookedFor(id):
    """
        Url serving DB data
    """
    query_result = storage.all(State)
    state = None
    for key, val in query_result.items():
        if val.id == id:
            state = val

    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
