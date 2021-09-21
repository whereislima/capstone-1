from flask import Flask, request, jsonify, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Product, Profile, Routine, RoutineStep
from forms import ProfileForm, RoutineForm, ProductForm

import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///betterskin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "puri-puri"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Render homepage."""

    return render_template("index.html")


@app.route("/API", methods=["GET", "POST"])
def call_API():

    form = ProductForm()
    if form.validate_on_submit():
        search_term = form.search_term.data


    url = "https://sephora.p.rapidapi.com/auto-complete"

    querystring = {"q": "serums"}

    headers = {
        'x-rapidapi-host': "sephora.p.rapidapi.com",
        'x-rapidapi-key': "4aff8a97ccmsh04b89d869aa3d1ap1fbf25jsn746679575818"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return("/")


@app.route("/profile", methods=["GET", "POST"])
def add_profile():

    form = ProfileForm()
    if form.validate_on_submit():
        age_range = form.age_range.data
        skin_type = form.skin_type.data
        skin_concerns = form.skin_concerns.data

        profile = Profile(age_range=age_range,
                          skin_type=skin_type, skin_concerns=skin_concerns)

        db.session.add(profile)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("profile_form.html", form=form)


@app.route("/routine", methods=["GET", "POST"])
def add_routine():
    form = RoutineForm()

    return render_template("routine_form.html", form=form)

@app.route("/product", methods=["GET", "POST"])
def add_product():

    form = ProductForm()
    if form.validate_on_submit():
        search_term = form.search_term.data

        url = "https://sephora.p.rapidapi.com/auto-complete" 

        querystring = {"q": search_term}

        headers = {
            'x-rapidapi-host': "sephora.p.rapidapi.com",
            'x-rapidapi-key': "4aff8a97ccmsh04b89d869aa3d1ap1fbf25jsn746679575818"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # print(response.text)
        jsonResp = response.json()
        print(jsonResp)
        for key, value in jsonResp.items():
            print(key)
            print(value)
            for term in value:
                print(term)
                for thing in term:
                    print(thing)
               
           
            

    return render_template("product_form.html", form=form)
