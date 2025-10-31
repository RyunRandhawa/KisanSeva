list1=['a', 'b', 'c']
list2=['h', 'i','t']
list3=['0', '1', '2']
print("Originally:")
print("List1=", list1)
print("List2=", list2)
print("List3=", list3)

list1.append(list2)
list1.insert(0,list3)
print("After adding two lists as individual elements, list now is:")
print(list1)