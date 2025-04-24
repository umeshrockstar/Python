#Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.
fa= open("sample2.txt", "r")
fb= open("hello2.txt","a+")
ch = fa.read(1)
while ch!="":
    fb.write(ch.upper())
    ch = fa.read(1)
fa.close()
fb.close()
print("Data copied successfully.")