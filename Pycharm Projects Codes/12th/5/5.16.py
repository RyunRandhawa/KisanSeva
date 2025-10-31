import pickle
stu={}
found = False
print("Searching in File student.dat...")
with open('student.dat', 'rb') as fin:
    try:
        while True:
            stu = pickle.load(fin)
            if stu['Marks'] > 81:
                print(stu)
                found = True
    except EOFError:
        pass
if found == False:
    print("No records with marks > 81")
else:
    print("Search successful")
    fin.close()