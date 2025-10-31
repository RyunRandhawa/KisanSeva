List = []

n = int(input("Enter the number of elements in the List: "))

print("Enter ",n," elements for the List: ")

for i in range(n):
    value = int(input())
    List.append(value)

List.sort()

print("Enter an element to be search: ")
element = int(input())

for i in range(n):
    if element == List[i]:
        print("Element found at Position:", i+1)