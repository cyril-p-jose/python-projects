#Programme to do simple calculations
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("OPTIONS\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Reminder")#To give the choice for calculation using menu driven
while True:
    c=int(input("Enter your choice:"))
    if c==1:
        print(a ,"+", b ,"=", a+b)
    elif c==2:
        print(a ,"-", b ,"=", a-b)
    elif c==3:
        print(a ,"*", b ,"=", a*b)
    elif c==4:
        print(a,"/",b ,"=", a/b)
    elif c==5:
        print("Reminder of", a,"/",b ,"=", a%b)
    else:
        print("Invalid choice")
        break
