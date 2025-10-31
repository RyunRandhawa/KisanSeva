import pickle
stu={}
stufile=open('student.dat', 'wb')
ans='y'
while ans == 'y':
    rno=int(input("Enter roll number:"))
    name=input("Enter name:")
    marks=float(input("Enter marks:"))
    stu['Rollno']=rno
    stu['Name']=name
    stu['Marks']=marks
    pickle.dump(stu, stufile)
    ans=input("Want to enter more records?(yes/no)...")
stufile.close()