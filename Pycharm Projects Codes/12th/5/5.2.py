myfile = open('poem.txt',"r")
s=myfile.readlines()
linecount=len(s)
print("Number of lines in poem.txt is", linecount)
myfile.close