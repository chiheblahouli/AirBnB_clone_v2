#!/usr/bin/python3
"""
Flask web application
"""


from flask import Flaskh
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
