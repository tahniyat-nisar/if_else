i=int(input("enter a number:"))
j=int(input("enter a number"))
if i>0 and j>0:
    sum=i+j
    if sum%5==0:
        print(sum)
    elif sum%5!=0:
        x=sum%5
        print(x)
        t=5-x
        print(t)
        print(t+sum)