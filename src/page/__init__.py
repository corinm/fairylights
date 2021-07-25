from flask import Flask, render_template

# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    apiUrl = "http://192.168.0.31:5001"
    return render_template("index.html", apiUrl=apiUrl)


def runPage():
    app.run(debug=True, host="0.0.0.0", port=5000)
