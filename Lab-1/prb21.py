#Calculate net salary
#where net salary = gross salary + allowance – deduction.
#Allowances are 10% while deductions are 3% of gross salary.
salary=int(input("Enter your your gross salary:"))

allowance=(10/100)*salary
deductance=(3/100)*salary


print("Salary received is",salary+allowance-deductance)
