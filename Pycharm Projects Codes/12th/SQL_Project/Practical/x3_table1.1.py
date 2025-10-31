import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

mycursor.execute("CREATE TABLE faculty_final (F_ID INTEGER(10) , FNAME varchar(50), LNAME varchar(50), HIRE_DATE varchar(50), SALARY INTEGER(10))")