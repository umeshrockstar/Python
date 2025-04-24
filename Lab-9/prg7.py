def ispalindrom():
    p=input("Enter any string:")
    n= p.lower() 
    n = n.replace(" ","") # to remove space
    p = n[::-1]
    if (p ==n):
        print("It is palindrome")
    else:
        print("It is not palindrome")


ispalindrom()
