"""
Foo Bar:: Ameer Alnasser, Wan Ying Li, Kevin Wang
SoftDev
k18 -- integrating sqlite3 into python
2022-10-26
time spent: 0.8 hrs
"""
import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


def courses_to_db():
    csvfile = open("courses.csv", "r")
    reader = csv.DictReader(csvfile)

    db.execute("DROP TABLE if exists courses;")
    c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);")
    for row in reader:
        c.execute(f'INSERT INTO courses VALUES("{row.get("code")}", {row.get("mark")}, {row.get("id")});')

def students_to_db():
    csvfile = open("students.csv", "r")
    reader = csv.DictReader(csvfile)
    
    db.execute("DROP TABLE if exists students")
    c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);")
    for row in reader:
        c.execute(f'INSERT INTO students VALUES("{row.get("name")}", {row.get("age")}, {row.get("id")});')

courses_to_db()
c.execute("SELECT * FROM courses;")
# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


#command = "CREATE TABLE talos"          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
