"""
importing from flask
"""
from flask import Flask, render_template

"""
this is needed so flask knows where to look up resources
"""
app = Flask(__name__)

"""
this is a decorator used to show flask what URL it'll trigger
"""


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


# in this format "/c/<text>/", it won't render in your browser rather it'll be 404
@app.route("/c/<text>/", strict_slashes=False)
def c(text):
    # replace all underscores with spaces
    return f"C {text.replace('_', ' ')}"


# added default parameter to be "is cool"
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>")
def python(text):
    # replace all underscores with spaces
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")