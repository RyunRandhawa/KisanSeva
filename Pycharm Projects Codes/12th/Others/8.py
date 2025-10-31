import csv
def write():
    with open("user.csv", 'w', newline='"') as f:
        w1 = csv.writer(f)
        w1.writerow(["UID", "Password"])
        while True:
            uid = input("Enter user-id: ")
            pswrd = input("Enter password: ")
            row = [uid, pswrd]
            w1.writerow(row)
            ch= input("Want to enter more? (y/n): ")
            if ch in 'nN':
                break

def read():
    try:
        with open("user.csv", 'r', newline='') as f:
            r1= csv.reader(f)
            print("Contents of the file:")
            for row in r1:
                print(row)
    except FileNotFoundError:
        print("The file 'user.csv' does not exist. Please write data first.")

def search():
    try:
        with open("user.csv", 'r', newline='') as f:
            r1= csv.reader(f)
            uidd = input("Enter the user-id whose password you want to search: ")
            for row in r1:
                if row[0] == uidd:
                    print(f"The password for user-id '{uidd}' is: {row[1]}")
                    return
            print(f"User-id '{uidd}' not found.")
    except FileNotFoundError:
        print("The file 'user.csv' does not exist. Please write data first.")
write()
read()
search()