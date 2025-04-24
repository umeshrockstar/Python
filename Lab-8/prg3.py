#Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.
s=set()
for i in range(5):
    b=input("Enter name:")
    s.add(b)
print(s)
lst = list(s)
lst.remove(lst[0])
a= input("Enter any new name:")
lst.append(a)
s1=set(lst)
print(s1)
lst= list(s1)
lst.remove(lst[0])
lst.remove(lst[1])
s1=set(lst)
print(s1)

