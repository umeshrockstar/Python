#Accept contact details from the user and create a vcard that we can directly store in our mobile
f = open("intro.vcf","a")
while True:
    nam = input("Enter the name (press Enter to stop): ")
    if not nam: 
        break
    gm= input("Enter the email: ")
    ph= input("Enter the phone number: ")
    ad= input("Enter the address: ")
    f.write("BEGIN:VCARD\n")
    f.write("Name:" + nam + "\n")
    f.write("EMAIL:" + gm + "\n")
    f.write("TEL:" + ph + "\n")
    f.write("ADR:" + ad + "\n")
    f.write("END:VCARD\n\n\n")
f.close()
