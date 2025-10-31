print("+ for ADDITION, ", "- for SUBTRACTION, ", " * for MULTIPLICATION, ", "/ for DIVISION, ", "n for Power value")
no = int(input("\nEnter the number of Inputs with which you want to do the operation(Max.5): "))

if no == 2:
    n1 = float(input("Enter The 1st Number:"))
    n2 = float(input("Enter The 2nd Number:"))

elif no == 3:
    n1 = float(input("Enter The 1st Number:"))

    n2 = float(input("Enter The 2nd Number:"))
    n3 = float(input("Enter The 3rd Number:"))

elif no == 4:
    n1 = float(input("Enter The 1st Number:"))
    n2 = float(input("Enter The 2nd Number:"))
    n3 = float(input("Enter The 3rd Number:"))
    n4 = float(input("Enter The 4th Number:"))

elif no == 5:
    n1 = float(input("Enter The 1st Number:"))
    n2 = float(input("Enter The 2nd Number:"))
    n3 = float(input("Enter The 3rd Number:"))
    n4 = float(input("Enter The 4th Number:"))
    n5 = float(input("Enter The 5th Number:"))

else:
    print("Minimum number with which operation can be done is 2 & Maximum number with which operation can be done is 5")
"+ - ADDITION"
"- - SUBTRACTION"
"* - MULTIPLICATION"
"/ - DIVISION"
"n-to the power"

user_input = input("Enter the Function to be used:")

if user_input == "+" and no == 2:
    n3 = 0
    n4 = 0
    n5 = 0

if user_input == "+" and no == 3:
    n4 = 0
    n5 = 0

if user_input == "+" and no == 4:
    n5 = 0

if user_input == "-" and no == 2:
    n3 = 0
    n4 = 0
    n5 = 0

if user_input == "-" and no == 3:
    n4 = 0
    n5 = 0

if user_input == "-" and no == 4:
    n5 = 0

if user_input == "*" and no == 2:
    n3 = 1
    n4 = 1
    n5 = 1

if user_input == "*" and no == 3:
    n4 = 1
    n5 = 1

if user_input == "*" and no == 4:
    n5 = 1

if user_input == "/" and no == 2:
    n3 = 1
    n4 = 1
    n5 = 1

if user_input == "/" and no == 3:
    n4 = 1
    n5 = 1

if user_input == "/" and no == 4:
    n5 = 1

if user_input == "+":
    output = n2 + n1 + n3 + n4 + n5
    print(output)
elif user_input == "-":
    output = n2 - n1 - n3 - n4 - n5
    print(output)
elif user_input == "*":
    output = n2 * n1 * n3 * n4 * n5
    print(output)
elif user_input == "/":
    output = n1 / n2 / n3 / n4 / n5
    print(output)
elif user_input == "n":
    output = n2 ** n1
    print(output)

else:
    print("!*!*! Invalid Entry !*!*!")