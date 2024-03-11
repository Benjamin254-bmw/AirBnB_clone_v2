#!/usr/bin/python3
"""
List of states
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def cities(id):
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    for state in states:
        if state.id == id:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html')


@app.teardown_appcontext
def closing(exc):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
