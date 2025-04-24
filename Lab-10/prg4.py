#Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.
fa = open("sample.csv", "r")
fb = open("hello.csv", "a+")
ch = fa.read(1)
while ch!= "":
    fb.write(ch)
    ch = fa.read(1)
fa.close()
fb.close()
print("Data copied successfully.")