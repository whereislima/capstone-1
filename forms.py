from wtforms import StringField, PasswordField, NumberField, FileField, SelectField
from wtforms.validators import InputRequired, Length, Optional, Email
from flask_wtf import FlaskForm


# class RegisterForm(FlaskForm):
#     """User registration form."""

#     username = StringField(
#         "Username",
#         validators=[InputRequired(), Length(min=1, max=20)],
#     )
#     password = PasswordField(
#         "Password",
#         validators=[InputRequired(), Length(min=6, max=55)],
#     )
#     email = StringField(
#         "Email",
#         validators=[InputRequired(), Email(), Length(max=50)],
#     )
#     first_name = StringField(
#         "First Name",
#         validators=[InputRequired(), Length(max=30)],
#     )
#     last_name = StringField(
#         "Last Name",
#         validators=[InputRequired(), Length(max=30)],
#     )

# class LoginForm(FlaskForm):
#     """Login form."""

#     username = StringField(
#         "Username",
#         validators=[InputRequired(), Length(min=1, max=20)],
#     )
#     password = PasswordField(
#         "Password",
#         validators=[InputRequired(), Length(min=6, max=55)],
#     )

class ProfileForm(FlaskForm):
    profile_image = FileField("profile image", Optional())
    age = NumberField("age", validators=[InputRequired()])
    skin_concerns = StringField("skin concerns", validators=[InputRequired()])

# information should come from the eBay API
class ProductForm(FlaskForm):
    name = TextField()
    price = NumberField()
    image = FileField()

class RoutineForm(FlaskForm):
    time_of_day = SelectField("time of day", validators=[InputRequired()], choices=[
                              ('morning', 'morning'), ('evening', 'evening')])
    frequency = SelectField("frequency", validators=[InputRequired()], choices=[
                            ('daily', 'daily'), ('weekly' 'weekly'), ('monthly', 'monthly')])
    step = NumberField("step", validators=[InputRequired()])
    type = SelectField("type", validators=[InputRequired()], choices=[('cleanser', 'cleanser'), ('essence', 'essence'), ('toner', 'toner'), ('serum', 'serum'), (
        'eyecream', 'eye cream'), ('moisturizer', 'moisturizer'), ('oil', 'oil'), ('active', 'active'), ('treatment', 'treatment'), ('mask', 'mask')])

