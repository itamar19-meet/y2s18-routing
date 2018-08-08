from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    query_all()
    return render_template(
        "home.html")

@app.route('/<int:student_id>')
def display_student(student_id):
    # add_student("bobobko",23562384792346297, True)
    # delete_student("itamar")

    return render_template(
        'student.html',
        student_id = student_id,
        student = query_by_id(student_id))

app.run(debug=True)

