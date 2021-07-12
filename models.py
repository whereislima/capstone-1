from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):

  __tablename__ = "products"
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  time_of_day = db.Column(db.Text, nullable=False)
  step = db.Column(db.Integer, nullable=False)
  type = db.Column(db.Text, nullable=False)



def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)