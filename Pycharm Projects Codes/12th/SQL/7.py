import pymysql

a = pymysql.connect(
    host="127.0.0.1",
    user="RyunRandhawa",
    password="R005911",
    database="test1"
)

mycursor = a.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Ryun", 22),
            ("Arya", 21),
            ("Sidhu", 28),
            ("Jia", 27),
            ("Michelle", 24)]

mycursor.executemany(sqlFormula, students)

a.commit()