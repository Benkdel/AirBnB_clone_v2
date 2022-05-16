#!/usr/bin/python3
"""
    Script to init flask application
"""

import sys
sys.path.append('../')
from models.state import State
from models.amenity import Amenity
from models.place import Place 
from models import storage
from flask import Flask, render_template



app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnbFilters():
    """
        Url serving DB data
    """

    """ load States and Cities """
    query_result = storage.all(State)
    states = []
    for key, val in query_result.items():
        states.append(val)

    """ load amenities """
    query_result = storage.all(Amenity)
    amenities = []
    for key, val in query_result.items():
        amenities.append(val)
    
    """ Places and Reviews """
    query_result = storage.all(Place)
    places = []
    for key, val in query_result.items():
        places.append(val)
    
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
