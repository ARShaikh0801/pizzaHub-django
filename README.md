# pizzaHub-django

A Django-based pizza ordering/demo application.

## Overview
pizzaHub is a Django web application for browsing a pizza menu and placing/demoing orders. It focuses on demonstrating common web app features such as CRUD for menu items and basic order flows.

## Features
- Menu listing (create, read, update, delete)
- Order creation and summary
- Admin interface for managing items
- Templates in HTML and styling with CSS

## Tech stack
- Python (Django)
- HTML, CSS
- (Optional) JavaScript for interactivity

## Prerequisites
- Python 3.8+
- pip
- (Optional) virtualenv

## Installation
1. Clone the repo:
   git clone https://github.com/ARShaikh0801/pizzaHub-django.git
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Apply migrations:
   python manage.py migrate
5. Create a superuser (for admin):
   python manage.py createsuperuser
6. Run the development server:
   python manage.py runserver

## Usage
- Open http://127.0.0.1:8000 in your browser.
- Visit `/admin` to manage menu items (use the superuser credentials).

## Env / Configuration
- If the project uses environment variables, create a `.env` or update `settings.py` with database and secret key settings.

## Contributing
- Fork -> branch -> PR. Follow Django best practices for changes and tests.

## Contact
- Maintainer: ARShaikh0801
