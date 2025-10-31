import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = ("Ryun", 22)

mycursor.execute(sqlFormula, student1)

a.commit()