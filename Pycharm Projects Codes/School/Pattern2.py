r = int(input("Enter the Limit: "))

for i in range(r):
    for s in range(i):
        print(end=" ")
    for c in range(r-i):
        print(c+1, end="")
    print("")