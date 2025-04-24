def pngr():
    n = 'abcdefghijklmnopqrstuvwxyz'
    str1=input("Enter  any string:")
    str2= str1.lower()
    c =0
    for i in n:
        if i in str2:
            c=c+1

    if c==26:
        print("It is pangram")
    else:
        print("It is not pangram")

pngr()
