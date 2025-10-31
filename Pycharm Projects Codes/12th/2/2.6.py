info={'Riya': 'CSC.', 'Mark': 'Eco', 'Ishpreet': 'Eng', 'Kamal': 'Env.Sc'}
inp=input("Enter value to be searched for:")
if inp in info.values():
    for a in info:
        if info[a]==inp:
            print("The key of given value is;",a)
else:
    print("Given value doesn't exist in dictionary.")