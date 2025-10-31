fileinp=open("Marks.txt","r")
while str:
    str=fileinp.readline()
    print(str)
fileinp.close()