from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")