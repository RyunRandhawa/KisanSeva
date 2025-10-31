list=[15,6,13,22,3,52,2]
print("Original list is;", list)
n=len(list)
for i in range(1,n):
    a=list[i]
    j=i-1
    while j>=0 and a<list[j]:
        list[j+1]=list[j]
        j=j-1
    else:
        list[j+1]=a
print("List after sorting:", list)