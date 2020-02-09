try:
    x=int(input("enter first num:"))
    y=int(input("enter second num:"))
    print("The result is:",x/y)
except BaseException as e:
    print("The type of execution:",type(e))
    print("The description is:",e)
