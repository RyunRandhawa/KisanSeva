dictionary = {}

while True:
    name = input("\nEnter name of friend: ")
    phone = int( input("Enter phone number of friend: "))
    dictionary[name] = phone

    quit = input("Enter Y to continue & N to Quit: ")
    if quit == "N" or quit == "n":
        break

#a
print()
print("a: ")
print(dictionary)

#b
print()
print("b: ")
name = input("Enter name of friend: ")
phone = int(input("Enter the NEW phone number of friend: "))
dictionary[name] = phone
print(dictionary)

#c
print()
print("c: ")
name = input("Enter name of that friend which you want to delete: ")
del dictionary[name]
print(dictionary)

#d
print()
print("d: ")
name = input("Enter name of that friend which you want to change his phone number: ")
phone = int(input("Enter phone number of friend: "))
del dictionary[name]
dictionary[name] = phone
print(dictionary)

#e
print()
print("e: ")
name = input("Enter name of that friend which you want to search: ")
if name in dictionary:
    print("Found")
else:
    print("Not Found")

#f
print()
print("f: ")
new_dictionary = {}
key = list(dictionary.keys())
key.sort()
for i in key:
    new_dictionary[i] = dictionary[i]
print(new_dictionary)