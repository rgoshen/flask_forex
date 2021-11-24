from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_from():
    return render_template("index.html")
