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
    print("Answer:",add(b,c))
if(a==2):
    print("Answer:",subtract(b,c))
if(a==3):
    print("Answer:",multiply(b,c))
if(a==4):
    print("Answer:",divide(b,c))
if(a>4):
    print("Option Invalid")
