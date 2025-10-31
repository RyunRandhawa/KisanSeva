r = int(input("Enter the Number of Rows: "))

for i in range(r):
    t = 65
    for j in range(i):
        print(chr(t),end='')
        t+=1
    print("")


r = int(input("\nEnter the Number of Rows: "))
t = 64
for i in range(r):
    for j in range(i):
        print(chr(t),end='')
    t += 1
    print("")