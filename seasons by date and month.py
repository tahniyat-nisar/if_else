date=int(input("enter date: "))
month=(input("enter month name:"))
if month in("december,january"):
   if date<=31:
       print( "your in winter season\nit's very cool")
elif month in ("feburary,march"):
    if date<=31:
        print("your in spring season\nit's sunny and pleasent")
elif month in ("april,may ,june"):
    if date<=31:
        print("your in summer season\nit's hot")
elif month in ("july,august"):
    if date<=31:
        print("your in monsoon\nit's wet,hot and humid")
elif month=="september":
    if date<=15:
        print("your in monsoon\nit's wet,hot and humid")
    elif date>=16 and date<=31:
        print("your in autumn\nit is pleasent")
elif month in ("october,november"):
    if date<=31:
        print("your in autumn\nit is pleasent")



