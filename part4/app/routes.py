from flask import Blueprint, render_template

# Blueprint frontend sans configuration spéciale
frontend = Blueprint("frontend", __name__)


@frontend.route("/")
def index():
    return render_template("index.html")


@frontend.route("/login")
def login():
    return render_template("login.html")
