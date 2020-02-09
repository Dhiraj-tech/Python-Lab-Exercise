print("enter a choice")
print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")
choice=int(input())
def add():
    x=int(input("first number"))
    y=int(input("second number"))
    z=x+y
    print(z)
def substraction():
    a=int(input("first number"))
    b=int(input("second number"))
    c=a-b
    print(c)
def multiplication():
    d=int(input("first number"))
    e=int(input("second number"))
    f=d*e
    print(f)
def division():
    g=int(input("first number"))
    h=int(input("second number"))
    i=g/h
    print(i)
if choice==1:
     add()
elif choice==2:
     substraction()
elif choice==3:
     multiplication()
elif choice==4:
     division()