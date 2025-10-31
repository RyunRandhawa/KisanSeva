def encrypt(sttr, enkey):
    return enkey.join(sttr)
def decrypt(sttr, enkey):
    return sttr.split(enkey)

mainstring=input("Enter main string:")
encryptStr=input("Enter encryption key:")
enStr=encrypt(mainstring, encryptStr)
deLst=decrypt(enStr, encryptStr)
deStr="".join(deLst)
print("The encrypted string is", enStr)
print("string after decryptio is:", deStr)