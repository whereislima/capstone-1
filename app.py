from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Product

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///products'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "good_skin"

connect_db(app)


@app.route("/")
def root():
    """Render homepage."""

    return render_template("index.html")