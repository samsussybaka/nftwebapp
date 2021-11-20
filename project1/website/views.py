#!/usr/bin/env python3

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Item, User
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
	offers = Item.query.all()
	return render_template("home.html", user=current_user, offers=offers)

@views.route("/sell", methods=['GET','POST'])
@login_required
def create_offer():
	if request.method == "POST":
		text = request.form.get('text')
		if not text:
			flash('Post created', category='success')
		else:
			offer = Item(text=text, seller=current_user.id)
			db.session.add(offer)
			db.session.commit()
			flash('Made Offer', category='success')
			return redirect(url_for('views.home'))
	return render_template("sell.html", user=current_user)