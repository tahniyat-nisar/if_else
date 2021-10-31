user_input=int(input("enter 1 digit or\n 2 digit or\n 3 digit or\n more digit number :"))
if user_input>=0 and user_input<=9:
    print("it is one digit number")
elif user_input>=10 and user_input<=99:
    print("it is two digit number")
elif user_input>=100 and user_input<=999:
    print("it is three digit number")
elif user_input>=1000:
    print("it is more than three digit number")



