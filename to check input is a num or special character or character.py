user_input=input("enter a letter or special character or number:-")
# Alphabet=input("enter a upper case letter:-")
if user_input>="A" and user_input<="Z":
    print("it is a capital letter")
    # alphabet=input("enter a lower case letter:-")
elif user_input>="a" and user_input<="z":
    print("it is a small letter")
    # special_character=input("enter a special character:-") 
elif user_input in ("~!@#$%&*+_|?/;:.,"):
     print("it is a special character ")
#      number=int(input("enter a number:-"))
# elif number>0:
#     print("it is a number")
elif int(user_input)>=0:
    print("it is a number")

