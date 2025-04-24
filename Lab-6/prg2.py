# A list contains tuples containing rollno, name and age of std.Wap to create three lists seperately for rollno,name and age
lst = [('24bcp192','hari','19'),('24bcp188','shyam','18'),('24bcp199','ram','20')]
lst1=[]
lst2=[]
lst3 =[]
for i in lst:
    lst1.append(i[0])
    lst2.append(i[1])
    lst3.append(i[2])
print(lst1)
print(lst2)
print(lst3)
