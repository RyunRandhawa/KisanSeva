import math

n = int(input("Enter the Number :"))
num1 = n
num2 = n

# Palindrome Number is a number that reads the same forward and backward.
reverse = 0
while num1>0:
    digit = num1 % 10
    reverse = reverse * 10 + digit
    num1 = int(num1/10)
if n == reverse:
    print(n, " is a Palindrome")
else:
    print(n, " is NOT a Palindrome")

#Armstrong Number is a number that is equal to the sum of the cubes of its own digits.
sum = 0
temp = num2
while temp > 0:
   digit = temp % 10
   sum += math.pow(digit,3)
   temp //= 10
if num2 == sum:
   print(num2, " is an Armstrong n")
else:
   print(num2, " is NOT an Armstrong n")


#Perfect Number is an integer that is equal to the sum of its proper divisors.
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 += i
if (sum1 == n):
    print(n, " is a Perfect Number")
else:
    print(n, " is NOT a Perfect Number")