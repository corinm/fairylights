from flask import Flask, render_template

# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello, World"
    return render_template("index.html", message=message)


def runPage():
    app.run(debug=True, host="0.0.0.0", port=5000)
