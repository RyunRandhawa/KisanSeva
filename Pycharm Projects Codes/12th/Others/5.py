import pickle
stu={}
stufile=open('student.dat', 'wb')
ans='yes'
while ans == 'yes':
    rno=int(input("Enter roll number: "))
    name=input("Enter name: ")
    marks=float(input("Enter Marks: "))
    stu['Rollno']=rno
    stu['Name']=name
    stu['Marks']=marks
    pickle.dump(stu, stufile)
    ans=input("Want to enter more records?(yes/no)...")
stufile.close()
searchkeys=int(input("Enter roll number to search: "))
updated = False
fin=open('student.dat','rb+')
records=[]

try:
    while True:
        stu=pickle.load(fin)
        if stu['Rollno'] == searchkeys:
            newmarks = float(input("Enter New Marks: "))
            stu['Marks'] == newmarks
            updated=True
        records.append(stu)

except EOFError:
    pass
    if updated:
        with open('student.dat', 'wb') as fout:
            for record in records:
                pickle.dump(record, fout)
        print("Record Successful Updated")
    else:
        print("No matching records found")
    fin.close()