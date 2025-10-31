import pymysql

a = pymysql.connect(
    host="localhost",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")