myfile=open("poem.txt","r")
lines=myfile.readlines()

file1=open("file1.txt","w")

for line in lines:
    if 'a' in line:
        file1.write(line)
myfile.close()
file1.close()