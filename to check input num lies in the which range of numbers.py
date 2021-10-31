number=int(input("enter a number above 100:"))
if number>=100 and number<=1000:
    print('the number lies in between 100 to 1000')
elif number>=1001 and number<=10000:
    print("the number lies in between 1000 to 10000")
elif number>=10001 and number<=50000:
    print("the number lies in between 10001 to 50000")
elif number>=50001 and number<=100000:
    print("the number lies in between 50000 to 100000")
else:
    print("enter the number below 100000 only")
