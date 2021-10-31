aryan=int(input("enter the age of aryan:"))
arjun=int(input("enter the age of arjun:"))
arav=int(input("enter the age of arav:"))
if (aryan<(arjun and arav)) and ((arjun and arav)>aryan) :
    print("aryan is younger brother of arjun and arav\narjun and arav are elder brothers of aryan")
elif (arjun<aryan and arav) and (aryan and arav>arjun):
    print("arjun is younger brother of aryan and arav\naryan and arav are elder brothers of arjun")
elif (arav<arjun and aryan) and (arjun and aryan >arav):
    print("arav is younger brother of aryan and arjun\narjun and aryan are elder brothers of arav")




