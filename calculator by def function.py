a=int(input("choice"))
x=int(input("1st num"))
y=int(input("2nd num"))
def add(x,y):
    c=x+y
    print(c)
def sub(x,y):
    c=x-y
    print(c)
def mult(x,y):
    c=x*y
    print(c)
def div(x,y):
    c=x/y
    print(c)
if a==1:
    add(x,y)
elif a==2:
    sub(x,y)
elif a==3:
    mult(x,y)
elif a==4:
    div(x,y)