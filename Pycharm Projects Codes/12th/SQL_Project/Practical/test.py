import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

sql1 = "UPDATE courses SET fees = fees + 500 WHERE CNAME = 'SYSTEM DESIGN'"

mycursor.execute(sql1)
final1 = mycursor.fetchall()

for x in final1:
        print(x)


#UPDATE COURSES
#SET FEES = FEES + 500
#WHERE CNAME = 'SYSTEM DESIGN';