#Pattern-1
print("Pattern-1")
l1 = int(input("Enter the Number of Rows: "))

for i in range(1,l1+1):
  for j in range(i):
    print('*',end='')
  print("")


#Pattern-2
print("\nPattern-2")
l2 = int(input("Enter the Number of Rows: "))

for i in range(l2):
  for j in range(l2-i):
    print('*',end='')
  print("")


#Pattern-3
print("\nPattern-3")
l3 = int(input("Enter the Number of Rows: "))

for i in range(l3):
  t = 65
  for j in range(i + 1):
    print(chr(t), end=' ')
    t += 1
  print("")