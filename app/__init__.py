from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

migrate = Migrate()
login_manager = LoginManager()
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"
    migrate.init_app(app, db)
    from .routes import main
    app.register_blueprint(main) # The system accepts "main" as the blueprint
    with app.app_context():
        db.create_all()
    return app

# Import the models after the db exists
from .models import (
    db,
    User,
    JournalEntry,
    MoodEntry,
    Resource
)
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))