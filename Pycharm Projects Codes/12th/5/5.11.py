import pickle
emp={}
empfile=open('Emp.dat','rb')
try:
    while True:
        emp=pickle.load(empfile)
        print(emp)
except EOFError:
    empfile.close()