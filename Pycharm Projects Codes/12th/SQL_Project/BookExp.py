import pymysql as cntr

import datetime as __dt
import matplotlib.pyplot as plt
from random import shuffle
from tempfile import mktemp
from os import system, startfile

db = cntr.connect(host='localhost',
                    user='RyunRandhawa',
                    passwd='R005911',
                    database='book_shop')
cur = db.cursor()

# Function to check is it leap year
is_leapyear = lambda year: year % 4 == 0


# Function to get last date of month
def last_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2 and is_leapyear(year):
        return 29
    elif month == 2:
        return 28
    else:
        return 30

clrscreen = lambda: system("cls")


def view_stock():
    cur.execute("select Book_No , Book_Name , Available_Stock from stock")
    data = cur.fetchall()
    # Print the table header
    print(f"{'Book Number':<15}{'Book Name':<25}{'Stock':<10}")
    # Iterate over the data and format each row
    for row in data:
        book_number = row[0]
        book_name = row[1]
        stock = row[2]
        print(f"{book_number:<15}{book_name:<25}{stock:<10}")


def add_stock():
    print('Add Stock'.center(89, '='))
    bno = unique_book_no()
    if bno:
        print("Book Number : ", bno)
    else:
        bno = int(input("Enter book number : "))
        bname = input("Enter the Book\'s Name : ")
        auth = input("Enter the Author of the Book : ")
        publ = input("Enter the Publisher of the Book : ")
        cost = eval(input("Enter the Cost per Book : "))
        stock = int(input("Enter the Quantity purchased : "))
    cur.execute(
        "insert into stock values ({} , '{}' , '{}' , '{}' , {} , {} , {} , '{}')".format(bno, bname,
                                                                                          auth, publ, cost,
                                                                                          stock, 0,
                                                                                          __dt.date.today()))
    print("Inserted Successfully !!!")


def add_user():
    user = input("Enter the user name : ")
    passwd = input("Enter a Password : ")
    passwd2 = input("Enter Password to confirm : ")
    if passwd == passwd2:
        cur.execute("insert into users values('{}' , '{}')".format(user, passwd))
        print("Created Successfully!!!")
    elif passwd != passwd2:
        print("You've entered different passwords")


def sell_book():
    print('Purchase')
    cname = input("Enter the Customer Name : ")
    phno = int(input("Enter the phone number : "))
    bno = int(input("Enter book number : "))
    bname = input("Enter the name of the book : ")
    cost = eval(input("Enter the cost of the book : "))
    cur.execute("insert into purchased values({} , '{}')".format(bno, __dt.date.today()))
    cur.execute("update stock set qty_purchased = qty_purchased + 1 where Book_No = {}".format(bno))
    cur.execute("update stock set Available_Stock = Available_Stock - 1 where Book_No = {}".format(bno))
    print("Bought Successfully")
    q = '''Book Shop\nName : {}\nPhone No : {}\nBook Number : {}\nBook Name : {}\nCost : {}\nDate Of Purchase : {}'''.format(
        cname, phno, bno, bname, cost, __dt.date.today())
    filename = mktemp('.txt')
    open(filename, 'w').write(q)
    startfile(filename, 'print')
    cur.execute('select Book_Name , Book_No , Author from stock where Available_Stock = 0')
    if cur.rowcount == 1:
        print("STOCK OF ")
        print("Book Name : ", cur.fetchall()[0][0])
        print("Book Number : ", cur.fetchall()[0][1])
        print("Author : ", cur.fetchall()[0][2])
        print("EXHAUSTED")
        cur.execute('delete from stock where Available_Stock = 0')


def unique_book_no():
    # Retrieve the maximum value of Book_No from the stock table
    cur.execute("select max(Book_No) from stock")
    data = cur.fetchall() # fetchone() is sufficient since we only need one row
    # If there are already book numbers, generate a unique one
    if bool(data[0][0]):
        # Create a range of possible book numbers starting after the maximum
        L1 = [x for x in range((data[0][0] + 1), (data[0][0] + 10000))]
        shuffle(L1)  # Shuffle to randomize
        return L1.pop(0) # Return the first number in the randomized list
    else:
        return False

# Graphs
def view_sales():
    print('Overall Sales This Month')
    cur.execute(
        "select distinct(s.Book_Name) , s.qty_purchased from stock s, purchased p "
        "where s.Book_No = p.Book_No and "
        "p.purchased_on between '{year}-{month}-01' and '{year}-{month}-{date}'".format(
            year=__dt.date.today().year,
            month=__dt.date.today().month,
            date=last_month(__dt.date.today().month, __dt.date.today().year)
        )
    )
    data = cur.fetchall()

    L1, L2 = [], []
    for row in data:
        L1.append(row[0])   # row[0] = Book_Name
        L2.append(row[1])   # row[1] = qty_purchased

    plt.bar(L1, L2)         # make a bar chart, x = book names, y = sales
    plt.xlabel('Books')     # x-axis label
    plt.ylabel('Sales')     # y-axis label
    plt.title('Sales')      # title
    plt.show()              # render the plot window


def login():
    user = input("Enter the username : ")
    pwd = input("Enter the password : ")
    cur.execute("select * from users where username = '{}' and password = '{}'".format(user, pwd))
    return bool(cur.rowcount)


def update_stock():
    bno = int(input("Enter the book number : "))
    cur.execute("select Book_Name , Available_Stock from stock where Book_No = {}".format(bno))
    data = cur.fetchall()
    print("Book Name : ", data[0][0])
    print("Available Stock : ", data[0][1])
    stock = int(input("Enter the new stock purchased : "))
    cur.execute("update stock set Available_Stock = Available_Stock + {}".format(stock))
    print("Updated Successfully")


def delete_stock():
    bno = int(input("Enter the book number: "))
        # First, delete all dependent rows in the `purchased` table
    cur.execute(f"DELETE FROM purchased WHERE Book_no = {bno}")
        # Then, delete the row from the `stock` table
    cur.execute(f"DELETE FROM stock WHERE Book_No = {bno}")
    print("Deleted Successfully")