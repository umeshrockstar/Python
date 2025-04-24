#Write a program that converts words present in a list into uppercase and stores them in a set.
lst = ['a','a','s','h','i','s','h']
lst1=[]
s={}
for i in lst:
    lst1.append(i.upper())
s = set(lst1)
print(s)
    