# 3.	Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from theimport random
import random
def nahsh():
    lst = []
    n = int(input("Enter the range: "))
    for i in range(n):
        b= random.randint(1,50)
        lst.append(b)
    p= list(set(lst))
    print(p)

nahsh()
