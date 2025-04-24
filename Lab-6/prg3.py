#Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.
d1= int(input("Enter the day: "))
m1= int(input("Enter the month: "))
y1= int(input("Enter the year: "))
d2= int(input("Enter the day: "))
m2= int(input("Enter the month: "))
y2= int(input("Enter the year: "))
t1= (d1,m1,y1)
t2= (d2,m2,y2)
if y1-y2 ==0:
    if m1-m2 ==0:
        print("The number of days between the two dates is: ",d1-d2)
    else:
        print("The number of days between the two dates is: ",(m1-m2)*30+(d1-d2))
else:
    print("The number of days between the two dates is: ",(y1-y2)*365+(m1-m2)*30+(d1-d2))
