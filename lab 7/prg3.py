#Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
dic = {1: {105: 10000, 102: 20000, 103: 30000}, 2: {107: 40000, 105: 50000, 106: 60000}}
n = len(dic)
for i in range(n):
    print("Department", i+1)
    print("Minimum Salary:", min(dic[i+1].values()))
    print("Maximum Salary:", max(dic[i+1].values()))
