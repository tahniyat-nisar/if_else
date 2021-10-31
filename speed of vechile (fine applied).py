user_input=int(input("enter speed of vechile in kmph:"))
if user_input>70:
    print(user_input-70)
    print("this is the amount of fine should be paid")
elif user_input<=70:
    print("stay home & stay safe")