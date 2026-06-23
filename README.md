# MellowSpace

MellowSpace is a mental wellbeing web application designed to help users manage their emotions, develop healthy coping strategies and build positive wellbeing habits.

The goal of MellowSpace is to provide a safe and supportive online space that helps users reduce the weight of emotions, one day at a time.

## Features

### Current Features

* User registration
* Secure password hashing using Flask-Bcrypt
* User authentication with Flask-Login
* Login and logout functionality
* PostgreSQL database integration
* Responsive navigation system
* Homepage and dashboard pages

### Planned Features

* Personal journal entries
* Mood tracking and mood history
* Wellbeing resource library
* Coping strategy guides
* Physical wellbeing activities
* User profiles
* Mental health self-help tools

## Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Bcrypt
* PostgreSQL

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Development Tools

* Git
* GitHub
* pgAdmin 4
* Visual Studio Code

## Database

MellowSpace uses PostgreSQL as its primary database.

Current database models include:

* User

Planned models include:

* JournalEntry
* MoodEntry
* Resource
* CopingStrategy

## Installation

### Clone the repository

```bash
git clone https://github.com/annawils441/mellowspace.git
cd mellow-space
```

### Create and activate a virtual environment

```bash
python -m venv myenv
```

Windows:

```bash
myenv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file and add:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=your-postgresql-connection-string
```

### Run the application

```bash
flask run
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## Project Status

This project is currently under active development as part of my software development portfolio.

## Authors

Anna Wilson
Thomas Powell
