date=int(input("enter the date: "))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
if year<=9000 and year>=1000:
    if month<=12 and month>=1:
        if date<=31 and date>=1:
            print(date+1,"/",month,"/",year)


