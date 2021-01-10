from logging import getLogger
from flask import render_template, redirect, url_for, request, flash
from . import auth_bp
from .. import models
from .forms import LoginForm, RegisterNewUserForm
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.urls import url_parse


logger = getLogger(__name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.get_by_email(form.email.data)
        if user is None or not user.verify_password(form.password.data):
            flash("Invalid username or password", "warning")
            return redirect(url_for("auth_bp.login"))
        user.authenticated = True
        login_user(user, remember=form.remember_me.data)
        next = request.args.get("next")
        if not next or url_parse(next).netloc != "":
            next = url_for("intro_bp.home")
        return redirect(next)
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    flash("You've been logged out", "light")
    return redirect(url_for("intro_bp.home"))


@auth_bp.route("/register_new_user", methods=["GET", "POST"])
def register_new_user():
    if current_user.is_authenticated:
        return redirect(url_for("intro_bp.home"))
    form = RegisterNewUserForm()
    if form.validate_on_submit():
        user = models.User(email=form.email.data, password=form.password.data)
        user.add_user(user)
        logger.debug(f"new user {form.email.data} added")
        return redirect(url_for("auth_bp.login"))
    return render_template("register_new_user.html", form=form)
