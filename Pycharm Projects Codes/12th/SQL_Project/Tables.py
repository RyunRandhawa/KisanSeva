import pymysql as cntr

# ------------------ DATABASE CONNECTION ------------------
db = cntr.connect(
    host='localhost',
    user='RyunRandhawa',
    passwd='R005911'
)
cur = db.cursor()

# ------------------ CREATE DATABASE ------------------
cur.execute("CREATE DATABASE IF NOT EXISTS book_shop")
cur.execute("USE book_shop")

# ------------------ CREATE TABLES ------------------

# STOCK TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS stock (
    Book_No BIGINT PRIMARY KEY,
    Book_Name VARCHAR(255),
    Author VARCHAR(255),
    Publisher VARCHAR(255),
    Cost_per_Book FLOAT,
    Available_Stock BIGINT,
    qty_purchased BIGINT,
    date_added DATE
)
""")

# USERS TABLE (fixed syntax)
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255)
)
""")

# PURCHASED TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS purchased (
    Book_No BIGINT,
    date_added DATE,
    FOREIGN KEY (Book_No) REFERENCES stock(Book_No)
)
""")

print("Database and tables created successfully!")

# ------------------ CLOSE CONNECTION ------------------
cur.close()
db.close()