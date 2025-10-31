f = open("../story.txt", 'r')

x = f.read()
v = c = lc = uc = sc = 0

for ch in x:
    if ch.islower():
        lc += 1
    if ch.isupper():
        uc += 1
    if ch.isalpha():
        if ch in 'aeiouAEIOU':
            v += 1
        else:
            c += 1
    else:
        sc += 1

f.close()

print("Uppercase:", uc)
print("Lowercase:", lc)
print("Vowels:", v)
print("Consonants:", c)
print("Special Characters:", sc)