from flask import render_template, request, redirect, url_for
import flask
import requests

from .forms import SignupForm

import json
import os


app = flask.Flask(__name__)
app.secret_key = "secret?"
app.debug = True


def add_user(email, password, identify):
    tsuru_host = os.environ.get("TSURU_HOST")
    url = "{}/users".format(tsuru_host)
    data = {
        "email": email,
        "password": password,
    }
    requests.post(url, data=json.dumps(data))


@app.route("/", methods=["GET", "POST"])
def index():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        add_user(form.email.data, form.password.data, form.identity.data)
        return redirect(url_for('help'))
    return render_template("index.html", form=form)


@app.route("/help")
def help():
    return render_template("help.html")
