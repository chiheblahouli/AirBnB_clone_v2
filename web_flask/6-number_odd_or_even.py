#!/usr/bin/python3
"""
Flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cisfun(text):
    """print text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """python is cool"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """displays n if is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def Numofhtml(n):
    """Number"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberoddoreven(n):
    """displays Pages only if n is an Integer"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html",
                               text="{} is even".format(n))
    else:
        return render_template("6-number_odd_or_even.html",
                               text="{} is odd".format(n))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
