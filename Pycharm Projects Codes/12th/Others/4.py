import pickle
stu={}
stufile=open('student.dat', 'wb')
ans='yes'
while ans == 'yes':
    rno=int(input("Enter roll number:"))
    name=input("Enter name:")
    stu['Rollno']=rno
    stu['Name']=name
    pickle.dump(stu, stufile)
    ans=input("Want to enter more records?(yes/no)...")
stufile.close()

fin=open('student.dat','rb')
searchkeys=int(input("Enter roll number to search: "))
found=False

try:
    print("Searching in File student.dat...")
    while True:
        stu=pickle.load(fin)
        if stu['Rollno'] == searchkeys:
            print(stu)
            found=True
            break

except EOFError:
    if found==False:
        print("No such records found in the file")
    else:
        print("Search successful.")
    fin.close()