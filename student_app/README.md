 Project Description
This project is a Student Performance Management System built using Python, Streamlit, and MySQL.
It allows users to add, view, update, delete, and analyze student performance data stored in a database.

Technologies Used
Frontend: Streamlit

Backend: Python

Database: MySQL

Libraries:

pandas

mysql-connector-python

matplotlib

Project Structure
student_app/
│
├── app.py              # Main Streamlit application
├── db.sql              # Database and table creation
├── requirements.txt    # Required Python libraries
├── README.md           # Project explanation
└── screenshots/        # Application screenshots
Database Design
Database Name
student_db
Table Name
students
Table Structure
Column Name	Description
id	Student ID (Primary Key)
name	Student Name
age	Student Age
subject	Subject Name
marks	Marks Obtained
⚙️ How the Code Works (app.py Explanation)
Database Connection
The function connect_db() is used to connect Python with MySQL.

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="student_db",
        auth_plugin="mysql_native_password"
    )
This connection is reused for all database operations.

Add Student
Takes Name, Age, Subject, Marks as input

Inserts the data into the students table

Purpose:
To store new student details in the database.

View Students
Fetches all student records from MySQL

Displays them in table format using st.dataframe()

Purpose:
To view all students stored in the database.

Pass / Fail Status
If marks ≥ 40 → Pass

If marks < 40 → Fail

A new column Status is added

Purpose:
To identify student performance easily.

Calculations
The application calculates:

Average Marks

Pass Percentage

Top Scorer

Purpose:
To analyze overall student performance.

Subject-wise Average
Groups students by subject

Calculates average marks for each subject

Purpose:
To compare performance across subjects.

Visualizations
Two charts are generated:

Bar Chart: Subject vs Average Marks

Pie Chart: Pass vs Fail Ratio

Purpose:
To visually represent student performance.

Update Marks
Takes Student ID and New Marks

Updates marks in the database

Purpose:
To modify existing student records.

Delete Student
Takes Student ID

Deletes the record from the database

Purpose:
To remove student data when required.

▶How to Run the Project
Install required libraries:

pip install -r requirements.txt
Create database and table:

Open MySQL Workbench

Run the code in db.sql

Run the application:

streamlit run app.py
Screenshots
All output screenshots of the application are stored in the screenshots folder.

Features Summary
Add student details

View all students

Update marks

Delete student record

Pass / Fail status

Average marks calculation

Pass percentage

Top scorer

Bar and Pie chart visualization

Conclusion
This project demonstrates how Streamlit can be used with MySQL to build a simple and interactive web application for managing and analyzing student performance data.