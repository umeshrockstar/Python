#Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.
s1=input("Enter a string:")
dic = {}
for i in s1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)