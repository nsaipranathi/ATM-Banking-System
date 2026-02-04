import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prana@2005",
        database="student_db",
        auth_plugin='mysql_native_password'
    )


st.title("Student Performance System")

st.header("Add Student")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1)
subject = st.text_input("Subject")
marks = st.number_input("Marks", min_value=0, max_value=100)

if st.button("Add Student"):
    db = connect_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO students (name, age, subject, marks) VALUES (%s,%s,%s,%s)",
        (name, age, subject, marks)
    )
    db.commit()
    st.success("Student added")

st.header("View Students")

db = connect_db()
query = "SELECT * FROM students"
df = pd.read_sql(query, db)
db.close()

if df.empty:
    st.warning("No student data found")
else:
    st.dataframe(df)

    # ---------- Pass / Fail ----------
    df["Status"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
    st.subheader("Pass / Fail Status")
    st.dataframe(df)

    # ---------- Calculations ----------
    st.subheader("Calculations")

    avg_marks = df["marks"].mean()
    pass_percent = (df[df["marks"] >= 40].shape[0] / df.shape[0]) * 100
    topper = df.loc[df["marks"].idxmax()]

    st.write("Average Marks:", avg_marks)
    st.write("Pass Percentage:", pass_percent)
    st.write("Top Scorer:", topper["name"])

    # ---------- Subject-wise Average ----------
    st.subheader("Subject-wise Average Marks")
    subject_avg = df.groupby("subject")["marks"].mean()
    st.dataframe(subject_avg)

    # ---------- Bar Chart ----------
    st.subheader("Bar Chart: Subject vs Average Marks")
    fig1, ax1 = plt.subplots()
    ax1.bar(subject_avg.index, subject_avg.values)
    ax1.set_xlabel("Subject")
    ax1.set_ylabel("Average Marks")
    st.pyplot(fig1)

    # ---------- Pie Chart ----------
    st.subheader("Pie Chart: Pass / Fail")
    fig2, ax2 = plt.subplots()
    df["Status"].value_counts().plot.pie(
        autopct="%1.1f%%",
        ax=ax2
    )
    ax2.set_ylabel("")
    st.pyplot(fig2)

# ---------- Update Marks ----------
st.header("Update Marks")

uid = st.number_input("Student ID", min_value=1, step=1)
new_marks = st.number_input("New Marks", min_value=0, max_value=100, step=1)

if st.button("Update Marks"):
    db = connect_db()
    cur = db.cursor()
    cur.execute(
        "UPDATE students SET marks=%s WHERE id=%s",
        (new_marks, uid)
    )
    db.commit()
    db.close()
    st.success("Marks updated successfully")

# ---------- Delete Student ----------
st.header("Delete Student")

did = st.number_input("Student ID to Delete", min_value=1, step=1)

if st.button("Delete Student"):
    db = connect_db()
    cur = db.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (did,))
    db.commit()
    db.close()
    st.warning("Student deleted successfully")