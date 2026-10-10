a=int(input("Choose your operation. 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division"))
b=int(input("Enter your first number"))
c=int(input("Enter your second number"))
def add(b,c):
    d=b+c
    return d
def subtract(b,c):
    d=b-c
    return d
def multiply(b,c):
    d=b*c
    return d
def divide(b,c):
    d=b/c
    return d
if(a==1):
    add(b,c)
if(a==2):
    subtract(b,c)
if(a==3):
    multiply(b,c)
if(a==4):
    divide(b,c)
if(a>4):
    print("Option Invalid")
