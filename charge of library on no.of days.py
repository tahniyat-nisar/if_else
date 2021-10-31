days=int(input("enter the number of days\nto calculate the charge of library:"))
if days<=5 and days>=1:
    print("Rs.2/day")
if days>=6 and days<=10:
    print("Rs.3/day")
if days>=11 and days<=15:
    print("Rs.4/day")
if days>15:
    print('Rs.5/day')