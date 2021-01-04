from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Length(1, 64), Email()],
        render_kw={"placeholder": "name@example.com"}
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    remember_me = BooleanField(" Keep me logged in")
    submit = SubmitField("Log In")


class RegisterNewUserForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Length(1, 64), Email()]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("confirm_password", message="Passwards must match")
        ]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired()]
    )
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.get_by_email(field.data):
            raise ValidationError("Email already registered")
