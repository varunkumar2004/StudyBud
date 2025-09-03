# StudyBud - Django Study Room Application

StudyBud is a web application built with Python and Django that allows users to create and join study rooms focused on various topics. It provides a platform for users to connect, chat, and share knowledge in a collaborative environment.

## Features

  * **User Authentication**: Secure user registration, login, and logout functionality.
  * **Room & Topic CRUD**: Users can Create, Read, Update, and Delete study rooms and topics.
  * **Real-time Chat**: Live messaging within study rooms for active discussions.
  * **User Profiles**: View and update user profiles.
  * **Search Functionality**: Easily search for specific rooms or topics.
  * **Recent Activity Feed**: See the latest messages and activities across the platform.
  * **Responsive Design**: A clean and modern user interface that works on all device sizes.

## Project Structure

```
studybud/
├── base/             # Main Django app for core logic (models, views, etc.)
├── studybud/         # Django project settings and configuration
├── static/           # Static files (CSS, JavaScript, images)
├── templates/        # HTML templates
├── db.sqlite3        # Development database
└── manage.py         # Django's command-line utility
```

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 1\. Prerequisites

  * Python 3.8+
  * `pip` (Python package installer)

### 2\. Installation & Setup

**1. Clone the Repository:**

```bash
git clone https://github.com/varunkumar2004/StudyBud.git
cd StudyBud
```

**2. Create and Activate a Virtual Environment:**
A virtual environment is recommended to keep project dependencies isolated.

```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate
```

**3. Apply Database Migrations:**
This will create the necessary database tables based on your models.

```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Create a Superuser (Admin):**
This allows you to access the Django admin panel.

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin username and password.

**5. Run the Development Server:**

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

  * **Register an Account**: Create a new user account to get started.
  * **Create a Room**: Start a new study room with a specific topic.
  * **Join a Discussion**: Browse existing rooms and join conversations.
  * **Admin Panel**: Access the admin interface at `/admin` to manage users, rooms, and topics directly.
