from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()

class Profile(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age_range = db.Column(db.Text, nullable=False)
    skin_type = db.Column(db.Text, nullable=False)
    skin_concerns = db.Column(db.Text, nullable=False)


class Product(db.Model):
  
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)

class Routine(db.Model):

    __tablename__ = "routines"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    time_of_day = db.Column(db.Text, nullable=False)
   
    products = db.relationship("Product", backref="products")

class RoutineStep(db.Model):

    __tablename__ = "routine_steps"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey("routines.id"), nullable=False)

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
