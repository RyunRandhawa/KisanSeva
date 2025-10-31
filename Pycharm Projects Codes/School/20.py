tup=(1,3,4,32)
c = 0
for i in tup:
    if tup.count(i) > 1:
        c += 1

if c > 1:
    print("Tuple contain duplicate element")
else:
    print("Tuple does NOT contain duplicate element")