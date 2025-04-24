def count_lower_upper():
    str = input("Enter any String:")
    c=0
    d=0
    for i in str:
        if i.isupper():
            c =c+1
        elif i.islower():
            d=d+1
    print("Upper Case:",c,"Lower Case:",d)

count_lower_upper()

