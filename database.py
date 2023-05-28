from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
db_path = "student_marks.db"

# Create the database and tables
def create_tables():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    date_of_birth TEXT,
                    parent_name TEXT,
                    address TEXT,
                    city TEXT,
                    phone_number TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject_name TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS grades (
                    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    grade_name TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS marks (
                    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade_id INTEGER,
                    marks_obtained INTEGER,
                    FOREIGN KEY (student_id) REFERENCES students (student_id),
                    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id),
                    FOREIGN KEY (grade_id) REFERENCES grades (grade_id)
                )''')
    conn.commit()
    conn.close()

# Insert a new student
def insert_student(details):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''INSERT INTO students (first_name, last_name, date_of_birth, parent_name, address, city, phone_number)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', details)
    conn.commit()
    conn.close()

# Insert marks for a student
def insert_marks(student_id, subject_id, grade_id, marks_obtained):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''INSERT INTO marks (student_id, subject_id, grade_id, marks_obtained)
                VALUES (?, ?, ?, ?)''', (student_id, subject_id, grade_id, marks_obtained))
    conn.commit()
    conn.close()

# Retrieve students with marks > 60%
def get_high_scoring_students():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''SELECT students.first_name, students.last_name
                FROM students
                JOIN marks ON students.student_id = marks.student_id
                WHERE marks.marks_obtained > 60''')
    result = c.fetchall()
    conn.close()
    return result

# Route for adding a new student
@app.route('/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        details = [
            request.form['first_name'],
            request.form['last_name'],
            request.form['date_of_birth'],
            request.form['parent_name'],
            request.form['address'],
            request.form['city'],
            request.form['phone_number']
        ]
        insert_student(details)
        return redirect('/students')
    return render_template('add_student.html')

# Route for adding marks for a student
@app.route('/add_marks/<int:student_id>', methods=['GET', 'POST'])
def add_marks(student_id):
    if request.method == 'POST':
        subjects = request.form.getlist('subject')
        grades = request.form.getlist('grade')
        marks = request.form.getlist('marks')

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        for i in range(len(subjects)):
            subject_id = int(subjects[i])
            grade_id = int(grades[i])
            marks_obtained = int(marks[i])
            c.execute('''INSERT INTO marks (student_id, subject_id, grade_id, marks_obtained)
                        VALUES (?, ?, ?, ?)''', (student_id, subject_id, grade_id, marks_obtained))

        conn.commit()
        conn.close()
        return redirect('/students')
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM subjects")
    subjects = c.fetchall()
    c.execute("SELECT * FROM grades")
    grades = c.fetchall()
    conn.close()
    
    return render_template('add_marks.html', student_id=student_id, subjects=subjects, grades=grades)

# Route for displaying students
@app.route('/students')
def display_students():
    students = get_high_scoring_students()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    create_tables()
    app.run()
