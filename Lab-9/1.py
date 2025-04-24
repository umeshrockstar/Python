def fun():
    print("This is fun function")
def disp():
    print("This is dis function")

def msg():
    print("This is msg function")

f=fun
d=disp
m=msg
l1=[f,d,m]

for i in l1:
    i()

