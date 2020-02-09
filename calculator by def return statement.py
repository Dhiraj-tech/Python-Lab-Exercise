print("enter your choice")
print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")
choice=int(input())
x=int(input("enter a 1st number"))
y=int(input("enter a 2nd number"))
def add(x,y):
    z=x+y
    return z
def substraction(a,b):
    c=a-b
    return c
def multiplication(d,e):
    f=d*e
    return f

def division(g,h):
    o=g/h
    return o

if (choice ==1):
    ans=add(x,y)
    print(ans)
elif (choice==2):
    m=substraction(x,y)
    print(m)
elif (choice==3):
    n=multiplication(x,y)
    print(n)
elif (choice==4):
    i=division(x,y)
    print(i)