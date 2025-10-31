import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

mycursor.execute("CREATE TABLE courses (C_ID varchar(50), F_ID INTEGER(10) , CNAME varchar(50), FEES INTEGER(10))")