t = int(input("Enter the Number of Terms: "))
n1= 0
n2 = 1
count = 0

if t <= 0:
   print("Please enter a positive integer")

else:
   print("Fibonacci Sequence: ")

   while count < t:
       print(n1, end=" ")
       next = n1 + n2
       n1 = n2
       n2 = next
       count += 1