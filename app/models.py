from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC
from app import db
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = "users"

    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False, unique=True)
    userEmail = db.Column(db.String(120), nullable=False, unique=True)
    passwordHash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))

    journalEntries = db.relationship("JournalEntry", backref="user", lazy=True) # Creates relationships
    mood_entries = db.relationship("MoodEntry", backref="user", lazy=True) # Creates relationships

    current_streak = db.Column(db.Integer, default=0) # For streak logging the mood diary entries
    longest_streak = db.Column(db.Integer, default=0) # For streak logging the mood diary entries
    last_entry_date = db.Column(db.Date) # For streak logging the mood diary entries

    def get_id(self): # Tells the program to user userID instead of id for "get_id()"
        return str(self.userID)
    
class JournalEntry(db.Model):
    __tablename__ = "journalentries"

    entryID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer,db.ForeignKey("users.userID"), nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))

class MoodEntry(db.Model):
    __tablename__ = "moodentries"

    moodID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer,db.ForeignKey("users.userID"), nullable=False)
    moodScore = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))

class Resource(db.Model):
    __tablename__ = "resources"

    resourceID = db.Column(db.Integer, primary_key=True)
    resourceTitle = db.Column(db.String(100), nullable=False)
    resourceDesc = db.Column(db.Text, nullable=False) # Description
    resourceCat = db.Column(db.String(25), nullable=False) # Category

class CopingFavourite(db.Model):
    __tablename__ = "copingfavourites"

    copingFavouriteID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey("users.userID"), nullable=False)
    strategyID = db.Column(db.String(100), nullable=False)