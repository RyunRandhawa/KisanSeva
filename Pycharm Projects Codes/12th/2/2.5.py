tuple1=('a', 'p', 'p', '1','e',)
char=input("Enter a single letter withut quotes:")
if char in tuple1:
    count=0
    for a in tuple1:
        if a != char:
            count += 1
        else:
            print(char, "is at index", count, "in", tuple1)
            break
else:
    print(char, "is NOT in", tuple1)