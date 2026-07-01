from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    Blueprint,
    request,
    jsonify
)
from app import db, bcrypt
from .forms import (
    RegistrationForm,
    LoginForm,
    MoodDiaryForm
)
from .models import (
    User, 
    MoodEntry,
    CopingFavourite
)
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
    LoginManager
) 
import calendar
from datetime import date, timedelta

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
    flash("You have been logged out.", "success")
    return redirect(url_for("main.homepage"))

@main.route("/dashboard")
@login_required # Requires log in functionality to be able to run this route
def dashboard():
    latest_entry = (
        MoodEntry.query.filter_by(userID=current_user.userID).order_by(MoodEntry.created_at.desc()).first()
    )
    today = date.today()
    mood_entries = MoodEntry.query.filter_by(userID=current_user.userID).all()
    total_entries = len(mood_entries)
    entries_this_month = [
        entry for entry in mood_entries
        if entry.created_at.month == today.month and entry.created_at.year == today.year
    ]
    entries_this_month_count = len(entries_this_month)
    # Average mood
    if entries_this_month:
        average_mood = round(sum(entry.moodScore for entry in entries_this_month) / entries_this_month_count, 1)
    else:
        average_mood = None
    # Last 3 mood entries query
    recent_entries = (
        MoodEntry.query.filter_by(userID=current_user.userID).order_by(MoodEntry.created_at.desc()).limit(3).all()
    )
    return render_template("dashboard.html", recent_entries=recent_entries,username=current_user.userName, latest_entry=latest_entry, total_entries=total_entries, entries_this_month=entries_this_month_count, average_mood=average_mood)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@main.route("/wellbeinglibrary")
def wellbeinglibrary():
    return render_template("wellbeing-library.html")

@main.route("/copingstrategies")
def copingstrategies():
    if current_user.is_authenticated:
        favourites = CopingFavourite.query.filter_by(userID=current_user.userID).all()
        favourite_ids = {
            favourite.strategyID
            for favourite in favourites
        }
    else:
        favourite_ids = set()
    return render_template("coping-strategies.html", favourite_ids=favourite_ids)

@main.route("/mooddiary", methods=["GET", "POST"])
@login_required
def mooddiary():
    form = MoodDiaryForm()
    today = date.today()
    if form.validate_on_submit():
        existing_entry = MoodEntry.query.filter(MoodEntry.userID == current_user.userID, db.func.date(MoodEntry.created_at) == today).first()
        if existing_entry:
            flash("You have already submitted a mood entry today.", "warning")
            return redirect(url_for("main.mooddiary"))
        entry = MoodEntry(
            userID = current_user.userID,
            moodScore = form.mood.data,
            notes = form.notes.data
        )
        db.session.add(entry)

        if current_user.current_streak is None: # Initialises the variables for accounts created before the DB changes
            current_user.current_streak = 0
        if current_user.longest_streak is None: # Initialises the variables for accounts created before the DB changes
            current_user.longest_streak = 0

        if current_user.last_entry_date is None:
            current_user.current_streak = 1
        elif current_user.last_entry_date == today:
            # Already logged today
            pass
        elif current_user.last_entry_date == today - timedelta(days=1):
            current_user.current_streak += 1
        else:
            current_user.current_streak = 1
        current_user.last_entry_date = today
        if current_user.current_streak > current_user.longest_streak: # Checks if the user's current streak is their longest streak
            current_user.longest_streak = current_user.current_streak
        message = None # Milestone streak message
        if current_user.current_streak == 1:
            message = "❤️ Great start!"
        elif current_user.current_streak == 3:
            message = "🌻 You're building a habit!"
        elif current_user.current_streak == 7:
            message = "🥳 One whole week! Well done!"
        elif current_user.current_streak == 14:
            message = "🌟 Two weeks! Congrats!"
        elif current_user.current_streak == 21:
            message = "😁 Three weeks! Yay!"
        elif current_user.current_streak == 30:
            message = "🤯 A whole month?! Go you!"
        db.session.commit()
        flash("Mood entry saved!", "success")
        if message:
            flash(message, "info")
        return redirect(url_for('main.mooddiary'))
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdatescalendar(
        today.year,
        today.month
    )
    entries = MoodEntry.query.filter_by(userID=current_user.userID).all()
    moods = {}
    for entry in entries:
        entry_date = entry.created_at.date() if hasattr(entry.created_at, 'date') else entry.created_at
        moods[entry_date] = {
            "score": entry.moodScore,
            "notes": entry.notes
        }
    return render_template("mood-diary.html", form=form, month_days=month_days, moods=moods, month=today.month)

@main.route("/legal")
def legal():
    return render_template("legal.html")

@main.route("/privacy")
def privacy():
    return render_template("privacy.html")

@main.route("/edit_username", methods=["POST"])
@login_required
def edit_username():
    new_username = request.form["username"]
    current_password = request.form["current_password"]
    # Check password input against current password in the User table
    if not bcrypt.check_password_hash(current_user.passwordHash, current_password):
        flash("Incorrect password.", "danger")
        return redirect(url_for("main.dashboard"))
    # Check if username belongs to another user
    existing_username = User.query.filter(User.userName == new_username, User.userID != current_user.userID).first()
    if existing_username:
        flash("That username is already taken.", "warning")
        return redirect(url_for("main.dashboard"))
    current_user.userName = new_username
    db.session.commit()
    flash("Username updated.", "success")
    return redirect(url_for("main.dashboard"))

@main.route("/edit_email", methods=["POST"])
@login_required
def edit_email():
    new_email = request.form["email"]
    current_password = request.form["current_password"]
    # Check password input against current password in the User table
    if not bcrypt.check_password_hash(current_user.passwordHash, current_password):
        flash("Incorrect password.", "danger")
        return redirect(url_for("main.dashboard"))
    # Check if email belongs to another user
    existing_email = User.query.filter(User.userEmail == new_email, User.userID != current_user.userID).first()
    if existing_email:
        flash("That email is already taken.", "warning")
        return redirect(url_for("main.dashboard"))
    current_user.userEmail = new_email
    db.session.commit()
    flash("Email updated.", "success")
    return redirect(url_for("main.dashboard"))

@main.route("/change_password", methods=["POST"])
@login_required
def change_password():
    current_password = request.form["current_password"]
    new_password = request.form["new_password"]
    confirm_password = request.form["confirm_password"]
    # Check password input against current password in the User table
    if not bcrypt.check_password_hash(current_user.passwordHash, current_password):
        flash("Incorrect password.", "danger")
        return redirect(url_for("main.dashboard"))
    if new_password != confirm_password:
        flash("Passwords do not match.", "warning")
        return redirect(url_for("main.dashboard"))
    else:
        hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
        current_user.passwordHash = hashed_password
        db.session.commit()
        flash("Password updated successfully.", "success")
        return redirect(url_for("main.dashboard"))
    
@main.route("/delete_account", methods=["POST"])
@login_required
def delete_account():
    current_password = request.form.get("current_password")
    # Check password input against current password in the User table
    if not bcrypt.check_password_hash(current_user.passwordHash, current_password):
        flash("Incorrect password.", "danger")
        return redirect(url_for("main.dashboard"))
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    flash("Your account has been deleted.", "info")
    return redirect(url_for("main.homepage"))

@main.route("/verify_password", methods=["POST"])
@login_required
def verify_password():
    data = request.get_json()
    password = data.get("password")
    if not bcrypt.check_password_hash(current_user.passwordHash, password):
        return jsonify({"valid": False})
    return jsonify({"valid": True})

@main.route("/toggle-favourite/<strategy_id>", methods=["POST"])
@login_required
def toggle_favourite(strategy_id):
    if not current_user.is_authenticated:
        return jsonify({"error": "Not logged in"}), 401
    favourite = CopingFavourite.query.filter_by(userID=current_user.userID, strategyID=strategy_id).first()
    if favourite:
        db.session.delete(favourite)
        favourited = False
    else: 
        db.session.add(
            CopingFavourite(
                userID = current_user.userID,
                strategyID = strategy_id
            )
        )
        favourited = True
    db.session.commit()
    return jsonify({"favourited": favourited})