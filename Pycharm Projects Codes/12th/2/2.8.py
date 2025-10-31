list=[15,6,13,22,3,52,2]
print("Original list is;", list)
n=len(list)
for i in range(n):
    for j in range(0,n-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("List after sorting:", list)