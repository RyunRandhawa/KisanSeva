import pymysql as cntr
import datetime as __dt
import matplotlib.pyplot as plt
from random import shuffle
from tempfile import mktemp
from os import system, startfile

# ======================== DATABASE CONNECTION ========================
db = cntr.connect(
    host='localhost',
    user='RyunRandhawa',
    passwd='R005911',
    database='book_shop'
)
cur = db.cursor()

# ======================== HELPER FUNCTIONS ===========================
is_leapyear = lambda year: year % 4 == 0

def last_month(month, year):
    """Returns last date of given month."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2 and is_leapyear(year):
        return 29
    elif month == 2:
        return 28
    else:
        return 30

clrscreen = lambda: system("cls")

# ======================== STOCK FUNCTIONS ============================

def view_stock():
    cur.execute("SELECT Book_No, Book_Name, Available_Stock FROM stock")
    data = cur.fetchall()
    print(f"{'Book Number':<15}{'Book Name':<30}{'Stock':<10}")
    print("-" * 55)
    for book_number, book_name, stock in data:
        print(f"{book_number:<15}{book_name:<30}{stock:<10}")


def unique_book_no():
    """Generate a new unique book number."""
    cur.execute("SELECT MAX(Book_No) FROM stock")
    data = cur.fetchone()
    if data[0]:
        next_no = data[0] + 1
    else:
        next_no = 1001
    return next_no


def add_stock():
    print('Add Stock'.center(89, '='))
    bno = unique_book_no()
    print(f"Book Number: {bno}")

    bname = input("Enter the Book's Name: ")
    auth = input("Enter the Author of the Book: ")
    publ = input("Enter the Publisher of the Book: ")
    cost = float(input("Enter the Cost per Book: "))
    stock = int(input("Enter the Quantity purchased: "))

    cur.execute(
        "INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (bno, bname, auth, publ, cost, stock, 0, __dt.date.today())
    )
    db.commit()
    print("✅ Book added successfully!")


def update_stock():
    bno = int(input("Enter the book number: "))
    cur.execute("SELECT Book_Name, Available_Stock FROM stock WHERE Book_No = %s", (bno,))
    data = cur.fetchone()

    if not data:
        print("❌ Book not found!")
        return

    print("Book Name:", data[0])
    print("Available Stock:", data[1])

    stock = int(input("Enter the new stock purchased: "))
    cur.execute("UPDATE stock SET Available_Stock = Available_Stock + %s WHERE Book_No = %s", (stock, bno))
    db.commit()
    print("✅ Stock updated successfully!")


def delete_stock():
    bno = int(input("Enter the book number to delete: "))
    cur.execute("DELETE FROM purchased WHERE Book_No = %s", (bno,))
    cur.execute("DELETE FROM stock WHERE Book_No = %s", (bno,))
    db.commit()
    print("✅ Book deleted successfully!")

# ======================== USER FUNCTIONS =============================

def add_user():
    user = input("Enter username: ")
    passwd = input("Enter password: ")
    passwd2 = input("Confirm password: ")

    if passwd != passwd2:
        print("❌ Passwords do not match!")
        return

    cur.execute("INSERT INTO users VALUES (%s, %s)", (user, passwd))
    db.commit()
    print("✅ User created successfully!")


def login():
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user, pwd))
    data = cur.fetchone()
    return bool(data)

# ======================== SALES FUNCTIONS ============================

def sell_book():
    print('Sell Book'.center(89, '='))
    cname = input("Enter Customer Name: ")
    phno = input("Enter Phone Number: ")
    bno = int(input("Enter Book Number: "))

    # Fetch book info
    cur.execute("SELECT Book_Name, Cost, Available_Stock FROM stock WHERE Book_No = %s", (bno,))
    data = cur.fetchone()

    if not data:
        print("❌ Book not found!")
        return

    bname, cost, stock = data
    if stock <= 0:
        print("⚠️ Book is out of stock!")
        return

    cur.execute("INSERT INTO purchased VALUES (%s, %s)", (bno, __dt.date.today()))
    cur.execute("UPDATE stock SET qty_purchased = qty_purchased + 1, Available_Stock = Available_Stock - 1 WHERE Book_No = %s", (bno,))
    db.commit()

    print("✅ Purchase recorded successfully!")
    receipt = f"""
    Book Shop Receipt
    -------------------------
    Customer: {cname}
    Phone: {phno}
    Book No: {bno}
    Book Name: {bname}
    Cost: ₹{cost}
    Date: {__dt.date.today()}
    -------------------------
    Thank you for shopping!
    """
    filename = mktemp('.txt')
    with open(filename, 'w') as f:
        f.write(receipt)
    startfile(filename, 'print')


def view_sales():
    print('Overall Sales This Month'.center(89, '='))
    cur.execute(
        "SELECT s.Book_Name, s.qty_purchased "
        "FROM stock s, purchased p "
        "WHERE s.Book_No = p.Book_No AND "
        "p.purchased_on BETWEEN %s AND %s",
        (f"{__dt.date.today().year}-{__dt.date.today().month}-01",
         f"{__dt.date.today().year}-{__dt.date.today().month}-{last_month(__dt.date.today().month, __dt.date.today().year)}")
    )

    data = cur.fetchall()
    if not data:
        print("No sales data for this month yet.")
        return

    books, sales = zip(*data)
    plt.bar(books, sales)
    plt.xlabel('Books')
    plt.ylabel('Units Sold')
    plt.title('Monthly Sales Report')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()
