import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 6")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)