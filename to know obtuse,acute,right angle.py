user_input=float(input("enter a angle of triangle\nto know wheather it is obtuse or acute or right angle: "))
if user_input>90:
    print("the angle is greater than 90 degrees\nso it is called obtuse angle of triangle")
elif user_input==90:
    print("the angle is equal to 90 degrees\nso it is called right angle of a triangle")
elif user_input<90:
    print("the angle is less than 90 degrees\nso it is called acute angle of a triangle")
