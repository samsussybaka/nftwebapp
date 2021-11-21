#!/usr/bin/env python3

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Item, User
from .__init__ import app
from . import db
import os

views = Blueprint("views", __name__)
UPLOAD_FOLDER = './upload_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

@views.route("/")
@views.route("/home")
@login_required
def home():
	return render_template("home.html", user=current_user)

@views.route("/sell", methods=['GET','POST'])
@login_required
def create_offer():
	if request.method == "POST":
		if 'file1' not in request.files:
			return 'theres no files uploaded'

		file1 = request.files['file1']
		path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
		return path


	return render_template("sell.html", user=current_user)




