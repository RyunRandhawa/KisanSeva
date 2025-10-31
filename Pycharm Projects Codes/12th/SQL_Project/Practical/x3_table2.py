import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

sql2 = "SELECT * FROM courses WHERE FEES BETWEEN 15000 AND 50000"

mycursor.execute(sql2)
final1 = mycursor.fetchall()

for x in final1:
        print(x)


#UPDATE COURSES
#SET FEES = FEES + 500
#WHERE CNAME = 'SYSTEM DESIGN';