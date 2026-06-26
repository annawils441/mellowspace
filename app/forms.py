from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    RadioField,
    TextAreaField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password") # Validates that the passwords are equal
        ]
    )
    submit = SubmitField("Create Account")

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField("Login")

class MoodDiaryForm(FlaskForm):
    mood = RadioField(
        "How are you feeling today?",
        choices = [
            (1, "😞 Very Low"),
            (2, "😟 Struggling"),
            (3, "😐 Okay"),
            (4, "🙂 Good"),
            (5, "🥰 Feeling Great")
        ],
        coerce=int,
        validators=[DataRequired()]
    )
    notes = TextAreaField(
        "Notes",
        validators=[Length(max=1000)]
    )
    submit = SubmitField("Save Entry")