import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

sql = "SELECT * FROM students WHERE name = 'Arya'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)