import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

sql1 = "SELECT * FROM faculty_final WHERE SALARY > 12000"
sql4 = "SELECT * FROM courses JOIN faculty_final ON courses.F_ID = faculty_final.F_ID WHERE FNAME = 'SULEKHA' ORDER BY CNAME DESC;"

mycursor.execute(sql1)
final1 = mycursor.fetchall()
mycursor.execute(sql4)
final2 = mycursor.fetchall()

for x in final1:
        print(x)
for y in final2:
        print(y)