r = int(input("Enter the Limit: "))

for i in range(r): #Upper
    for s in range(r-i): #Space
        print(end=" ")

    for j in range(i): #Printing
        print("*",end=" ")
    print("")


for i in range(r): #Lower
    for s in range(i): #Space
        print(end=" ")

    for j in range(r-i): #Printing
        print("*", end=" ")
    print("")