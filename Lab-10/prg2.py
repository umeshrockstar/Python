#Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects.
#  Also calculate total. Display the dictionary data on the monitor.
f= open("sample.csv","r")
d= f.readlines()   
f.close() 
for line in d:
    details = line.strip().split(",") 
    rollno, nme, cpII, mathii, eee = details  
    student_dict = {
        "Roll No": rollno,
        "Name": nme,
        "Marks": [cpII, mathii, eee]  
    }

    print(student_dict)