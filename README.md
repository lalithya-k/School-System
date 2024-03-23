# School Management System

## Overview

The School Management System is a web application developed using Flask, MongoDB, and HTML/CSS. It allows administrators to manage student records, including registration, authentication, and viewing all students' information. The system provides a user-friendly interface for both administrators and students.

## Features

- User authentication: Admin login with username and password.
- Student registration: Form to input student details such as name, date of birth, contact information, etc.
- Admin dashboard: View all registered students and their details.
- Responsive design: Designed using HTML/CSS for a user-friendly experience across devices.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/lalithya-k/school-management-system.git
```

2. Install dependencies:

```
pip install flask flask-pymongo
```

3. Run the Flask application:

```
python app.py
```

4. Access the application in your web browser:

```
http://localhost:5000
```

## File Structure

- `app.py`: Python script containing the Flask application code.
- `templates/`: Directory containing HTML templates for rendering web pages.
- `static/`: Directory containing static files such as CSS stylesheets and images.
- `requirements.txt`: File listing all Python dependencies.

## Technologies Used

- Flask: Python web framework for building the backend.
- MongoDB: NoSQL database for storing student records.
- HTML/CSS: Frontend design and user interface.
- PyMongo: Python library for interacting with MongoDB from Flask.

## Usage

1. Login as admin using the provided credentials.
2. Register new students by filling out the registration form.
3. View all registered students on the admin dashboard.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and expand upon this README file with additional details specific to your project.
