month_num=int(input("enter the month number\nfrom 1 to 12 only:"))
if month_num in (4,6,9,11):
    print("enter this month has 30 days")
elif month_num==2:
    print("enter this month has 28 days")
else:
    print("enter this month has 31 days")

