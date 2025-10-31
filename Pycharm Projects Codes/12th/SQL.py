import mysql.connector
def connect_to_db():
    """Establish a connection to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1008$&2007",
        database="BrewJoint" )

def order_total(order, contents):
    return sum(contents [item] for item in order if item in contents)

A=connect_to_db()
if A.is_connected():
    c=A.cursor()
    c.execute("SELECT item_name, price FROM MENU")
    contents={item[0].lower(): float(item[1]) for item in c.fetchall()}
print("***********************")
print("WELCOME TO 'BREW JOINT'")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~ \n Here's our menu:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

for item, price in contents.items():
    print(f"{item.title()}: ${price}")

order = []
while True:
    item= input("What would you like to have? ").strip().lower()
    if item in contents:
        order.append(item)
        print (f"Your item {item.title()}' has been added to your order.")
    else:
        print (f"Sorry, (item.title()) is not available.")

    another = input("Do you want to add something else? (Yes/No) ").capitalize()

    if another != "Yes":
        break

total = order_total(order, contents)
print("\nHere's your bill:")

for item in order:
    print(f"{item.title()}: {contents [item]}")

has_coupon = input("Do you have any coupons? (Yes/No) ").capitalize()
if has_coupon == "Yes":
    discount = total * 0.25 # 25% discount
    total -= discount
    print(f"\nCoupon applied! You received a 25% discount of round(discount, 2)).")

taxes = total*0.12
total+=taxes
print("\nFinal Bill:")

for item in order:
    print(f"{item}: ${contents[item]}")
print(f"Taxes (12%): ${round(taxes, 2)}")
if has_coupon == "Yes":
    print(f"Discount: -${round(discount, 2)}")
print(f"Your total amount to pay is ${round(total, 2)}")
print("~~~~~~~~~~~~~~~~\nThanks for your visit!!!!\n~~~~~~~~~~~~~~~~\nHave a nice day.")
c.close()
A.close()