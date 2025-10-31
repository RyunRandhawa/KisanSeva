#Compute the greatest common divisor and least common multiple of two integers
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
i = 1

#GCD
while(i <= n1 and i <= n2):
  if(n1 % i == 0 and n2 % i == 0):
    gcd = i
  i = i + 1
print("Greatest Common Divisor (GCD): ", gcd)

# LCM 
if n1 > n2:
    g = n1
else:
    g = n2

while(True):
    if((g % n1 == 0) and (g % n2 == 0)):
        lcm = g
        break
    g += 1
print("The Least Common Multiple (LCM): ", lcm)



#Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
S = input("\nType the String: ")
vc = 0
cc = 0
vowel = set("aAeEiIoOuU")

#Vowels & Consonants Count
for alpha in S:
    if alpha in vowel:
        vc += 1
    elif alpha == ' ':
        cc = cc
    else:
        cc += 1

print("Number of Vowels in", S, ": ", vc)
print("Number of Consonants in", S, ": ", cc)

# Upper & Lower Count
uc = 0
lc = 0
for e in S:
    if e.isupper():
        uc += 1
    elif e.islower():
        lc += 1

print("Number of UPPER Case in", S, ": ", uc)
print("Number of lower case in", S, ": ", lc)