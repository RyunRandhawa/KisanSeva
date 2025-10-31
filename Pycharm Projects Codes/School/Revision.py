for i in range(2,101,2):
    print(i)


print('Red','Green','Blue', sep=',', end='@')
print('JATT')


x = "apple"
if "p" not in x:
    print("True")
else:
    print("False")


print(x.capitalize())
print(x[2:5:2])


print(x.find("le"))

print(x.isalnum(), end=', '), print(x.isalpha(), end=', '), print(x.isdigit(), end=', '), print(x.isspace())
print(x.islower(), end=', '), print(x.isupper())

print(x.lower(), end=', '), print(x.upper())

print(x.lstrip("al"), end=', '), print(x.rstrip("l"))
print(x.lstrip()) #Removes Whitespace


#Odd or Even
x = int(input("Enter the Number: "))
if x/2 == True:
    print("Even")
else:
    print("Odd")