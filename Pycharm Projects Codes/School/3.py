a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3nd number: "))

#Greatest
if a>b:
    if a>c:
        print("Greatest: ",a)
    else:
        print("Greatest: ",c)

else:
    if b>c:
        print("Greatest: ",b)
    else:
        print("Greatest: ",c)

#Smallest
if a<b:
    if a<c:
        print("Smallest: ",a)
    else:
        print("Smallest: ",c)

else:
    if b<c:
        print("Smallest: ",b)
    else:
        print("Smallest: ",c)