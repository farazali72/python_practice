a = int(input("Enter the first integer:"))
b = int(input("Enter the second integer: "))
c = int(input("Enter the thrid integer: "))

if(a>b) and (a>c):
    print("A value is highest: ", a)
elif(b>a) and (b>c):
    print("B value is highest: ", b)
else:
    print("C value is highest: ", c)