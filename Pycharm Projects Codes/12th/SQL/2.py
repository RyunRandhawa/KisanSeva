import pymysql

a = pymysql.connect(
    host="localhost",
    user="RyunRandhawa",
    password="R005911"

)

mycursor = a.cursor()

mycursor.execute("CREATE DATABASE test1")