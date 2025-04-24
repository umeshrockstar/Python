#A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.
s={'Arpan','arpit','Bibek','bishal'}
s1=set()
s2=set()
for i in s:
    if i.startswith('a'):
        s1.add(i)
    if i.startswith('b'):
        s2.add(i)
    if i.startswith('B'):
        s2.add(i)
    if i.startswith('A'):
        s1.add(i)
print(s1)
print(s2)
