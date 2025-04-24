#Write a program to create a csv file that we can directly open in MS-Excel.
f = open("sample.csv", "w")  
while True:
    rollno = input("Enter the roll number (press Enter to stop): ")
    if not rollno: 
        break

    nme = input("Enter the name: ")
    cpII, mathii, eee = input("Enter the marks of Python, Maths, and EEE: ").split(" ")

    f.write(rollno + "," + nme + "," + cpII + "," + mathii + "," + eee + "\n")

f.close()
print("Data saved successfully.")
