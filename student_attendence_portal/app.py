import streamlit as st
import mysql.connector
import pandas as pd
from datetime import date
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prana@2005",
        database="student_portal"
    )
st.header("Add Student")

with st.form("student_form"):
    roll = st.text_input("Roll No")
    name = st.text_input("Name")
    clas = st.selectbox("Class", ["Class 1", "Class 2", "Class 3"])
    submit = st.form_submit_button("Add Student")

if submit:
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO students (roll_no, name, class) VALUES (%s, %s, %s)",
        (roll, name, clas)
    )
    con.commit()
    st.success("Student added successfully!")
st.header("Mark Attendance")

con = get_connection()
df = pd.read_sql("SELECT * FROM students", con)

student = st.selectbox("Select Student", df['name'])
status = st.radio("Attendance Status", ["Present", "Absent"])
att_date = st.date_input("Date", date.today())

if st.button("Submit Attendance"):
    sid = df[df['name'] == student]['id'].values[0]
    cur = con.cursor()
    cur.execute(
        "INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)",
        (sid, att_date, status)
    )
    con.commit()
    st.success("Attendance recorded!")
st.header("Add Marks")

subject = st.selectbox("Subject", ["Maths", "Science", "English"])
marks = st.number_input("Marks", 0, 100)

if st.button("Add Marks"):
    sid = df[df['name'] == student]['id'].values[0]
    cur = con.cursor()
    cur.execute(
        "INSERT INTO marks (student_id, subject, marks) VALUES (%s, %s, %s)",
        (sid, subject, marks)
    )
    con.commit()
    st.success("Marks added!")
st.header("Attendance History")

att_df = pd.read_sql("""
SELECT s.name, a.date, a.status
FROM attendance a
JOIN students s ON a.student_id = s.id
""", con)

st.dataframe(att_df)
st.header("Attendance Percentage")

query = """
SELECT s.name,
(COUNT(CASE WHEN a.status='Present' THEN 1 END) / COUNT(*)) * 100 AS percentage
FROM attendance a
JOIN students s ON a.student_id = s.id
GROUP BY s.name
"""
percent_df = pd.read_sql(query, con)
st.dataframe(percent_df)
st.header("Pass / Fail Status")

pf_df = pd.read_sql("""
SELECT s.name, AVG(m.marks) as avg_marks,
CASE WHEN AVG(m.marks) >= 40 THEN 'Pass' ELSE 'Fail' END AS result
FROM marks m
JOIN students s ON m.student_id = s.id
GROUP BY s.name
""", con)

st.dataframe(pf_df)
