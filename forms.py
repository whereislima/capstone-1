from wtforms import StringField, PasswordField, NumberField, FileField, SelectField
from wtforms.validators import InputRequired, Length, Optional, Email
from flask_wtf import FlaskForm



class RegisterForm(FlaskForm):
    """User registration form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
    )

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )

class ProfileForm(FlaskForm):
    profile_image = FileField("profile image", Optional())
    age = NumberField("age", validators=[InputRequired()])
    skin_concerns = StringField("skin concerns", validators=[InputRequired()])

class RoutineForm(FlaskForm):
    time_of_day = SelectField()
    step = NumberField()
    type = SelectField()


