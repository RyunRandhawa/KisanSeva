import pickle
stu={}
found=False
fin=open('student.dat','rb')
searchkeys=[12,14]

try:
    print("Searching in File student.dat...")
    while True:
        stu=pickle.load(fin)
        if stu['Rollno'] in searchkeys:
            print(stu)
            found=True
except EOFError:
    if found==False:
        print("No such records found in the file")
    else:
        print("Search successful.")
    fin.close()