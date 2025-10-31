import mysql.connector

a = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jatt123",
    database="PRACTICAL"
)

mycursor=a.cursor()

mycursor.execute("SELECT * FROM faculty_final")

final = mycursor.fetchall()

for x in final:
        print(x)