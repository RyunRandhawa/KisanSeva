myfile = open("poem.txt","r")
for line in myfile:
    for word in line.split():
        print(word, end='#')
    print()
myfile.close()