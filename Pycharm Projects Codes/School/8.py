# Python Program to check whether string is palindrome or not
s = input("Enter a string: ")
w = ""

for element in s[::-1]:
    w += element

if (s == w):
    print(s, "is a Palindrome string")
else:
    print(s, "is NOT a Palindrome string")



# Python Program to convert the case of characters in a string
s = input("\nEnter a string: ")
w = ""

for element in s[::1]:

    if element.isupper():
        w += element.lower()
    else:
        w += element.upper()

print(w)