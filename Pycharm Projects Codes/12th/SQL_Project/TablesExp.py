import pymysql as cntr

db = cntr.connect(host='localhost',
                  user='RyunRandhawa',
                  passwd='R005911')

cur = db.cursor()

# Creates Database
cur.execute("create database if not exists book_shop")
cur.execute("use book_shop")

# Create Stock Table
cur.execute("""create table stock 
            (
            Book_No bigint primary key,
            Book_Name varchar(255),
            Author varchar(255),
            Publisher varchar(255),
            Cost_per_Book float,
            Available_Stock bigint,
            qty_purchased bigint,
            date_added date 
            )
            """)

# Create User Table
cur.execute("""create table 
            (
            users(username varchar(255), 
            password varchar(255)
            )
            """)

# Create Purchased Table
cur.execute("""create table purchased (
            Book_no bigint, 
            date_added date, 
            foreign key(Book_no) references stock(Book_No)
            )
            """)

print("Database and Tables created successfully")

cur.close()
db.close()