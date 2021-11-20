#!/usr/bin/env python3

from flask import Blueprint, render_template, request, redirect, url_for
views = Blueprint(__name__, "views")



@views.route("/")
def home():
    return render_template("index.html", name="Tim")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))


