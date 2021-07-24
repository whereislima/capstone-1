from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()

class Routine(db.Model):

  __tablename__ = "routines"
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  time_of_day = db.Column(db.Text, nullable=False)
  products = db.relationship("Product")

class Product(db.Model):

  __tablename__ = "products"
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, nullable=False)
  type = db.Column(db.Text, nullable=False)
  price = db.Column()
  image = db.Column()

class Step(db.Model):

  __tablename__ = "steps"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
  routine_id = db.Column(db.Integer, db.ForeignKey("routines.id"), nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)