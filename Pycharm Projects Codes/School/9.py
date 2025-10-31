List = []

n = int(input("Enter the number of elements in the List: "))

print("Enter ",n," elements for the List: ")

for i in range(n):
    value = int(input())
    List.append(value)

List.sort()

print("Largest element in the List:", max(List))
print("Smallest element in the List:", min(List))
