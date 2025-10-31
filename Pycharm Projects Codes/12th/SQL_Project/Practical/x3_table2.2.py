import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

sqlFormula =  "INSERT INTO courses (C_ID, F_ID, CNAME, FEES) VALUES (%s, %s, %s, %s)"
courses = [("C21", 102, "GRID COMPUTING", 40000),
           ("C22", 106, "SYSTEM DESIGN", 16000),
           ("C23", 104, "COMPUTER SECURITY", 8000),
           ("C24", 106, "HUMAN BIOLOGY", 15000),
           ("C25", 102, "COMPUTER NETWORK", 20000),
           ("C26", 105, "VISUAL BASICS", 6000),]

mycursor.executemany(sqlFormula, courses)

a.commit()