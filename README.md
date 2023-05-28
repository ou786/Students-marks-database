# Students-marks-database

# Student Marks Management System

This is a web-based Student Marks Management System built with Flask and SQLite. It allows users to add new students, record their marks for multiple subjects, and display students with marks higher than 60%.

## Features

- Add new students with their personal details such as name, date of birth, parent name, address, city, and phone number.
- Record marks for multiple subjects for each student.
- Store subjects and grades in the database.
- Retrieve and display students who have obtained marks higher than 60%.

## Requirements

- Python 3.x
- Flask framework
- SQLite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ou786/student-marks-database.git
```

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Create the database tables:

```bash
python app.py
```

6. Run the application:

```bash
flask run
```

7. Open your web browser and go to `http://localhost:5000` to access the application.

## Usage

- Access the homepage to add a new student by filling in the required details.
- To add marks for a student, click on the student's name in the Students list.
- In the Add Marks page, select the subject, grade, and marks obtained for each subject.
- Click the "Add Marks" button to record the marks.
- You can view the list of students who have obtained marks higher than 60% by navigating to the Students page.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/)
