from wtforms import StringField, PasswordField, DecimalField, IntegerField, FileField, SelectField
from wtforms.validators import InputRequired, Length, Optional, Email
from flask_wtf import FlaskForm


class ProfileForm(FlaskForm):
    age_range = SelectField("generational age", validators=[InputRequired()], choices=[('genA', 'Alpha'), ('genZ', 'Zoomer'), ('genY', 'Millenial'), ('genX', 'GenX'), ('gen', 'Boomer')])
    skin_type = SelectField("skin type", validators=[InputRequired()], choices=[('oily', 'oily'), ('dry', 'dry'), ('combination', 'combination')])
    skin_concerns = SelectField("skin concerns", validators=[InputRequired()], choices=[('acne', 'acne breakouts'), ('aging', 'aging, wrinkles, fine lines'), ('pigmentation', 'pigmentation, sun damage'), ('sensitive', 'sensitive, dry, redness') ])

# information should come from the eBay API
class ProductForm(FlaskForm):
    search_term = StringField(("search term"), validators=[InputRequired()])

class RoutineForm(FlaskForm):
    time_of_day = SelectField(("morning or evening"), validators=[InputRequired()], choices=[('morning', 'morning'), ('evening', 'evening')])
    # add products


