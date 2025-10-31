import pickle
stu={}
with open('student.dat', 'rb') as fin:
    try:
        print("File student.dat stores these records")
        while True:
            stu=pickle.load(fin)
            print(stu)
    except EOFError:
        fin.close()