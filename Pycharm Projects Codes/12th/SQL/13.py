import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

sql = "UPDATE students SET age = 19 WHERE name = 'Arya'"

mycursor.execute(sql)

a.commit()