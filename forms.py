from wtforms import StringField, PasswordField, DecimalField, IntegerField, FileField, SelectField
from wtforms.validators import InputRequired, Length, Optional, Email
from flask_wtf import FlaskForm


class ProfileForm(FlaskForm):
    age = IntegerField("age", validators=[InputRequired()])
    skin_type = SelectField("skin concerns", validators=[InputRequired()], choices=[('oily', 'oily'), ('dry', 'dry'), ('combination', 'combination')])
    skin_concerns = SelectField("skin concerns", validators=[InputRequired()], choices=[('acne', 'acne'), ('wrinkles', 'wrinkles'), ('pigmentation', 'pigmentation')])

# information should come from the eBay API
class ProductForm(FlaskForm):
    search_term = StringField(("search term"), validators=[InputRequired()])

class RoutineForm(FlaskForm):
    name = StringField(("name of routine"), validators=[InputRequired()])


class StepForm(FlaskForm):
    number = IntegerField()
    name = StringField()
    description = StringField()
    price = DecimalField()
