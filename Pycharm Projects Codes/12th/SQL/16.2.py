import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

sql = "DELETE FROM students WHERE age = 27"

mycursor.execute(sql)

a.commit()