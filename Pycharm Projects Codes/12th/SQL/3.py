import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911"
)

mycursor = a.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)