from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    Blueprint
)
from app import db, bcrypt
from .forms import (
    RegistrationForm,
    LoginForm
)
from .models import User
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
    LoginManager
) 

main = Blueprint("main", __name__) # Creates a blueprint for the routes
login_manager = LoginManager()

@main.route("/")
def homepage():
    return render_template("index.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8") # Password Bcrypt Security
        user = User(
            userName = form.username.data,
            userEmail = form.email.data,
            passwordHash = hashed_password
        )
        existing_user = User.query.filter_by(userEmail=form.email.data).first() # Checks if the email is unique
        if existing_user:
            flash("An account with this email already exists.")
            return render_template("register.html", form=form)
        else:
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully!", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userEmail = form.email.data).first() # Filters by email to find the user
        if user and bcrypt.check_password_hash(user.passwordHash, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Invalid email or password")
    return render_template("login.html", form=form)

@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.homepage"))

@main.route("/dashboard")
@login_required # Requires log in functionality to be able to run this route
def dashboard():
    return render_template("dashboard.html", username=current_user.userName)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@main.route("/wellbeinglibrary")
def wellbeinglibrary():
    return render_template("wellbeing-library.html")

@main.route("/copingstrategies")
def copingstrategies():
    return render_template("coping-strategies.html")

@main.route("/mooddiary")
@login_required
def mooddiary():
    return render_template("mood-diary.html")

@main.route("/legal")
def legal():
    return render_template("legal.html")