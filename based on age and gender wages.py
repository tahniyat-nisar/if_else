age=int(input("enter age upto 40 only:"))
gender=(input("enter as M for male and F for female:"))
if age>=18 and age<30:
   if gender=="M":
        print("wage/day=700")
   elif gender=="F":
            print("wage/day=750")
elif age>=30 and age<=40:
    if gender=="M":
        print("wage/day=800")
    elif gender=="F":
            print("wage/day=850")