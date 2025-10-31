myfile= open("poem.txt", "r")
str = ""
vcount = 0
ccount = 0
while True:
    str = myfile.read(1)
    if not str:
        break
    if str.isalpha():
        if str in ['a', 'A', 'e', 'E', 'i', 'I', 'o', '0', 'u', 'U']:
            vcount += 1
        else:
            ccount += 1
myfile.close()
print("Vowels in the file:", vcount)
print("Consonants in the file:", ccount)
myfile.close()