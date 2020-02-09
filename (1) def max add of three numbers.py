def max():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    c=int(input("enter 3rd number"))
    if a>b>c:
            print(a,"is max for all")
    elif b>c>a:
         print(b,"is max for all")
    else:
        print(c,"is max for all")
max()