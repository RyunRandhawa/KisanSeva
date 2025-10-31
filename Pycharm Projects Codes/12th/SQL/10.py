import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

mycursor.execute("SELECT age FROM students")

myresult = mycursor.fetchone()

for x in myresult:
    print(x)