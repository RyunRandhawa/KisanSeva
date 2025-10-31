list = []

n = int(input("Enter the number of elements in the List: "))

print("Enter ",n," elements for the List: ")

for i in range(n):
    value = int(input())
    list.append(value)

#Printing Original List
print("The original list : " + str(list))

# Separating Odd and Even  elements
oe = []
ee = []

for i in range(0, len(list)):
    if i % 2:
        ee.append(list[i])

    else:
        oe.append(list[i])

result = oe + ee

#Printing Final List
print("Separated odd and even index list: " + str(result))