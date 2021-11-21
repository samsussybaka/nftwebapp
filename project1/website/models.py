from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))
	date_created = db.Column(db.DateTime(timezone=True), default=func.now())

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	price = db.Column(db.Integer(), nullable=False)
	date_created = db.Column(db.DateTime(timezone=True), default=func.now())
	seller = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
