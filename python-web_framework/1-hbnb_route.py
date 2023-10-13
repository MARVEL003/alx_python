"""
importing from flask
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")