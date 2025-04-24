#Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
lst= [("apple", 50), ("banana", 30), ("orange", 40), ("grapes", 60)]
n = len(lst)
for i in range(n):
    for j in range(n-i-1):
        if lst[j][1] < lst[j+1][1]:
            lst[j+1], lst[j] = lst[j], lst[j+1]
print(lst)
    
        
    