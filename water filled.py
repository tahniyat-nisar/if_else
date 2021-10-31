
water=int(input("enter how many liters"))
if water<1:
    print("more water need to be filled") 
elif water>1 and water<10:
    print("no need to fill water")
else:
    print("water is overflowed")