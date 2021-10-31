attendence=int(input('enter number of classes attended:'))
classes_held=int(input ('enter number of classed held:'))
if ((attendence/classes_held)*100)<75:
    print(attendence/classes_held*100,'%')
    print("student is  not allowed to sit in exam")
elif (attendence/classes_held*100)>=75 and (attendence/classes_held*100)<=100:
    print(attendence/classes_held*100,"%")
    print("student is allowed to sit in exam")



