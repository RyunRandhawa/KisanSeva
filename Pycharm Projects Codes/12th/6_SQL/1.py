import mysql.connector
#Connect to the database
con = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Jatt123',
    database='empdata'
    )

if con.is_connected():
    cur = con.cursor()
    while True:
        No = int(input("Enter Employee Number: "))
        Name = input("Enter Employee Name: ").strip()
        Gender = input("Enter Employee Gender (M/F): ").strip().upper()
        Salary = int(input("Enter Employee Salary: "))
        Query = "INSERT INTO EMP (No, Name, Gender, Salary) VALUES ((), '{}', '{}', ()".format(No, Name, Gender, Salary)
        cur.execute(Query)
        con.commit()
        print("Record stored successfully!")
        opt = input("Do you want to add another employee? (y/n): ").strip().lower()
        if opt != 'y':
            break
    print("\nAll Employee Records:")
    cur.execute("SELECT FROM EMP")
    for record in cur.fetchall():
        print(record)

    cur.close()