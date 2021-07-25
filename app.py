from flask import Flask, request, jsonify, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Product
from forms import ProfileForm, RoutineForm, ProductForm

API_BASE_URL = "https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search?q=skincare"

# should keep in a secret file
access_token = "Bearer v^1.1#i^1#f^0#p^1#I^3#r^0#t^H4sIAAAAAAAAAOVYe2wURRi/6wsKFMIbTTWXlRABd28f99xwh3ctpUdaWrgWzyLW2d3Z69K93cvOrO2FILXRaoyEBANGkKQx0aR/KJHEKGJFE0z0HzVKRCoQEyVClJAYUxE0ce56lGslpbRnbOLmksvMfM/ffPN93wzbU1G5pq++7/cq56yS/h62p8Tp5OaylRXla+eXltxb7mALCJz9PSt7ynpLL61DIKWnxa0QpU0DQVd3SjeQmJsMUbZliCZAGhINkIJIxLIYjzQ2iDzDimnLxKZs6pQrVhuiApwq8BBIwM+DQEDykFnjpswWM0T5PT5e8qpSkJUVLyfxZB0hG8YMhIGBQxTP8hzN+mnO28LyIk9+HkbgfG2Uaxu0kGYahIRhqXDOXDHHaxXYOrGpACFoYSKECscidfGmSKx2w+aWde4CWeE8DnEMsI3GjmpMBbq2Ad2GE6tBOWoxbssyRIhyh0c0jBUqRm4aMwXzc1D7Bb/fJ8EgAILPE+TUokBZZ1opgCe2IzujKbSaIxWhgTWcuROiBA1pJ5RxfrSZiIjVurJ/W2yga6oGrRC1IRp5NNLcTIUbtEZAJ01TQZ2aQcejCToQ8PgEmeNYmgtKXp+kCnklI5LyEI/TUmMaipYFDLk2mzgKicVwPC5cAS6EqMlosiIqzlpTSOcZxU9oy27oyA7auMPI7ilMERBcueGd0R/lxtjSJBvDUQnjF3LwhCiQTmsKNX4xF4f50OlGIaoD47Todnd1dTFdAmNaSTfPspw70dgQlztgClB52uxZ70banRloLeeKDAkn0kScSRNbukmcEgOMJBUWfAEf58njPtas8PjZf0wU+OweexqKdToEOSizASAEBB+QAkApxukI5wPUnbUDSiBDp4DVCXFaBzKkZRJndgpamiIKXpUXAiqkFV9QpT1BVaUlr+KjORVCFkJJkoOB/8shmWyYx6FsQVy0OC9KjCdREDc0dCWauPhGpS6Z6KiDPoFraE3Gos3R+ubmxkTSbIoLnNWWDE32JNzW+RpdI8i0EP3FBCB71qcPQr2JMFSm5V5cNtOw2dQ1OTOzNliwlGZg4UzUzpBxHOo6+ZuWq5F0Ola8bF0UJ+8iUUzN5+JWqP+gOt3WK5QN2pnlVZYfEQEgrTHZ+sPIZsptAtJ4uLNnnUy356x2TUA4SuSW7AyTtCHCxBKF9H6TZtJIImdIKVMmzzJSKIkTk2chFwvFlvGUFOUqMkPQ1JIdGN2Vzu7pgCLZeue0gk4jF4YZFXLE3RG/NWWk02dyzjPoSZmxIDJti1xymKZs89tidkKDtBPYMnUdWtu4aSfSVMrGQNLhTMuoRcguGph6r1PW63z/X/GL8/Gkv/H6PdPzTc51M+0zrSYUsw7exX3GPfZlJezIfVyvc5DtdR4vcTpZP9G/ll1dUdpaVjqPQiSTMAgYimR2MxpQGZLEDIBtCzKdMJMGmlVS4dSGTsvXCt50+newK0ZfdSpLubkFTzxs9a2Vcm7B8iqeY/2cl+XJ52ljH7i1WsYtK1uiXbr+lzXY2vHZ81/uOD3Atw8P/Olgq0aJnM5yBwlAh/nTUOWV67jtqqNp3/rFn99/4sIzP/iHnvhN37jplX0hu+a9Dd+fuoyG245dePDgh4e3Xzv7QnX9Hn2g9jX6xJJu9N2RtxadOjuYPP9JzaeNZcOzuoa/nTP7uZVfXeYOvN0zzG1/es+BVbv36Q5H9NzqPamXv76aXnpjRRDtGqo65T15cdPOvnfCy5fNX7D/xTPqHMfueT/ec8B8YXBX4iBv/bymum3nu3WLqxdXNAw8Ej35zUfB2FOLLv5xfK/9qv2LunfrB/a5w5z48bKlCx+/+uazW4/Erjhay9bPXlC70J24kZjfHi05e6gl5tjdeeilLQ9v3HKm8fT+o7+ueoM+tv38QPVDj31xX1//60fDLSPb+DedPsUnbRMAAA=="

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///products'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "puri-puri"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Render homepage."""

    return render_template("index.html")

@app.route("/profile", methods=["GET", "POST"])
def add_profile():

    form = ProfileForm()

    return render_template("profile_form.html", form=form)

@app.route("/product", methods=["GET", "POST"])
def add_routine():

    form = ProductForm()

    return render_template("product_form.html", form=form)

@app.route("/routine", methods=["GET", "POST"])
def add_routine():

    form = RoutineForm()

    return render_template("routine_form.html", form=form)

