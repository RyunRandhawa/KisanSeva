import pickle
stu={}
found = False
with open('student.dat', 'rb+') as fin:
    try:
        while True:
            rpos=fin.tell()
            stu = pickle.load(fin)
            if stu['Rollno'] == 12:
                stu['Name']='Gurnam'
                fin.seek(rpos)
                pickle.dump(stu, fin)
                fin.flush()
                found = True
    except EOFError:
        pass
if found == False:
    print("Sorry, no matching record found.")
else:
    print("Record(s) successfully updated.")
fin.close()