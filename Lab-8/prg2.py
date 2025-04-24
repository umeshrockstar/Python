#Write a program to create a set containing 10 random numbers in the range 15 to 45.
#Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
import random
s=set()
for i in range(10):
    s.add(random.randint(15,45))
print(s)
lst = [i for i in s if i >= 30]
s1=set(lst)
print(s1)