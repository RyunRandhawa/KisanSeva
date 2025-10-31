count=int(input("How many students are there in the class?"))
fileout=open("Marks.txt","w")

for i in range(count):
    print("Enter details for student", (i+1), "below:")
    rollno=int(input("Roll no:"))
    name=input("Name:")
    marks=float(input("Marks:"))
    rec=str(rollno)+", "+name+", "+str(marks)+'\n'
    fileout.write(rec)
fileout.close()