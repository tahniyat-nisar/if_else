arti=int(input('enter age of arti:'))
gayatri=int(input("enter age of gayatri:"))
vaishnavi=int(input("enter age of vaishnavi:"))
if (arti>gayatri and vaishnavi):
    print("arti is elder")
elif gayatri<vaishnavi:
        print('vaishnavi is second elder\ngayatri is younger')
if vaishnavi>gayatri:
            print("gayatri is second elder\nvaishnavi is younger")
elif gayatri>arti and vaishnavi:
    print("gayatri is elder")
if arti<vaishnavi:
        print("vaishnavi is second elder\narti is younger")
elif arti>vaishnavi:
            print("arti is second elder\nvaishnavi is younger")
if vaishnavi>arti and gayatri:
    print("vaishnavi is elder")
elif arti<gayatri:
    print("gayatri is second elder\n arti is younger")
if arti>gayatri:
    print("arti is second elder\n gayatri is younger")     