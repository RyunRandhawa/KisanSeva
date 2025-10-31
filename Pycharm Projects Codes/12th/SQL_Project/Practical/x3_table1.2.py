import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

sqlFormula =  "INSERT INTO faculty_final (F_ID, FNAME, LNAME, HIRE_DATE, SALARY) VALUES (%s, %s, %s, %s, %s)"
faculty_final = [(102, "AMIT", "MISHRA", "12-10-1998", 12000),
                 (103, "NITIN", "VYAS", "24-12-1994", 8000),
                 (104, "RAKSHIT", "SONI", "18-05-2001", 14000),
                 (105, "RASHMI", "MALHOTRA", "11-09-2004", 11000),
                 (106, "SULEKHA", "SRIVASTAVA", "05-06-2006", 10000),]

mycursor.executemany(sqlFormula, faculty_final)

a.commit()