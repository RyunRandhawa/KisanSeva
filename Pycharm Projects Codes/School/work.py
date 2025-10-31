print("Program-1")
n = int(input("Enter the Number: "))
l = int(input("Enter the Limit: "))

for i in range(1, l+1):
    print(n*i)


print("\nProgram-2")
r = int(input("Enter the Number of Rows: "))

for i in range(r):
    t=1
    for j in range(r-i):
        print(t,end='')
        t += 1
    print("")