import pymysql as cntr

db = cntr.connect(host='localhost',
                  user='RyunRandhawa',
                  passwd='R005911')

cur = db.cursor()

# Creates Database
cur.execute("CREATE DATABASE IF NOT EXISTS book_shop")
cur.execute("USE book_shop")

# Create Stock Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        Book_No BIGINT PRIMARY KEY,
        Book_Name VARCHAR(255),
        Author VARCHAR(255),
        Publisher VARCHAR(255),
        Cost FLOAT,
        Available_Stock BIGINT,
        qty_purchased BIGINT,
        date_added DATE
    )
""")

# Create User Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255)
    )
""")

# Create Purchased Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS purchased (
        Book_No BIGINT,
        purchased_on DATE,
        FOREIGN KEY (Book_No) REFERENCES stock(Book_No)
    )
""")

print("Database and Tables created successfully")

cur.close()
db.close()
