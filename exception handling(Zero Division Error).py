try:
    a=int(input("enter first:"))
    b=int(input("enter second:"))
    print(a/b)
except ArithmeticError as e:
    print(type(e))
    print(e)
    print(e.__class__)
    print(e.__class__.__name__)
print("over")
