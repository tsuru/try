import flask
from flask import render_template, request

from .forms import SignupForm


app = flask.Flask(__name__)
app.secret_key = "secret?"
app.debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    form = SignupForm(request.form)
    return render_template("index.html", form=form)


@app.route("/help")
def help():
    return "help"
