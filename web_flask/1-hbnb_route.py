#!/usr/bin/python3
"""a script that starts a Flask web application:

web application is listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display `HBNB`
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns a greeting for the user """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
