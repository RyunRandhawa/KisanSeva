import csv
fh=open("Employee.csv","w", newline="")
ewriter=csv.writer(fh)
empdata=[
    ['Empno', 'Name', 'Designation', 'Salary'],
    [1001, 'Trupti', 'Manager', 56000],
    [1002, 'Raziya', 'Manager', 55900],
    [1003, 'Simran', 'Analyst', 35000],
    [1004, 'Silviya', 'Clerk', 25000],
    [1005, 'Suji', 'PR Officer', 31000]
]
ewriter.writerows (empdata)
print("File successfully created")
fh.close()