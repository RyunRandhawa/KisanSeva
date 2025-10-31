import pickle
stu={}
fin=open('student.dat','rb')
try:
    print("Filestudent.dat stores these records")
    while True:
        stu=pickle.load(fin)
        print(stu)
except EOFError:
    fin.close()