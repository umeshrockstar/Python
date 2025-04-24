#Wap that define a fnc sum_avg() to accept the marks of 5 sub and calc the average and total.
def sum_avg():
    n = int(input("Enter the number of subjects:"))
    sum= 0
    for i in range(1,n+1):
        i = int(input(f"Enter the marks of {i}subject:"))
        sum=sum+i
    avg_marks = sum/n
    total_marks = sum
    print(f"Total marks={total_marks} and Average Marks={avg_marks}")

sum_avg()
