# 4.Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.
import random
def nubnn():
    lst =[]
    lst1=[]
    lst2=[]
    n = int(input("Enter the numbers that you want:"))
    for i in range(n):
        p = random.randint(-100,100)
        lst.append(p)
    print(lst)
    for i in lst:
        if(i <0):
            lst1.append(i)
    for i in lst:
        if(i>0):
            lst2.append(i)
    print(lst1)
    print(lst2)
        
nubnn()

    
