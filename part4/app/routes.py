from flask import Blueprint, render_template

# On indique à Flask que les templates sont dans le dossier 'templates' à la racine
frontend = Blueprint("frontend", __name__, template_folder="../templates")


@frontend.route("/")
def index():
    return render_template("index.html")


@frontend.route("/login")
def login():
    return render_template("login.html")
