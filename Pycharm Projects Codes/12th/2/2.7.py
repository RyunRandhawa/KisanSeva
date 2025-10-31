info={'Riya': 'CSc.', 'Mark': 'Eco', 'Ishpreet': 'Eng', 'Kamal': 'Env.Sc'}
inp=input("Enter value to be searched for:")
for a in info:
    if info[a].upper()==inp.upper():
        print("The key of given value is",a)
        break
else:
    print("Given value doesn't exist in dictionary.")