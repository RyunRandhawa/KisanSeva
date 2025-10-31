line=input("Enter a line:")
lowercount = uppercount = 0
digitcount = alphacount = 0

for a in line:
    if a.isalpha():
        alphacount+=1
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1

print("Number of Uppercase Letters:", uppercount)
print("Number of Lowercase Letters:", lowercount)
print("Number of Alphabets:", alphacount)
print("Number of Digits:", digitcount)