user_input=input("enter a capital or small letter:")
if user_input>="A" and user_input<='Z':
    print("entered letter is capital letter")
elif user_input>="a" and user_input<="z":
    print("entered letter is small letter")
else:
    print("please enter a letter only")