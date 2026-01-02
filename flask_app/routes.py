from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already exists", "danger")
        elif User.query.filter_by(email=form.email.data).first():
            flash("Email already registered", "danger")
        else:
            user = User(
                full_name=form.full_name.data, # type: ignore
                email=form.email.data, # type: ignore
                username=form.username.data, # type: ignore
                password_hash=generate_password_hash(form.password.data) # type: ignore
            )
            db.session.add(user)
            db.session.commit()
            flash("Account created! You can now log in.", "success")
            return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data): # type: ignore
            login_user(user)
            return redirect(url_for("main.profile"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)

@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.full_name)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
