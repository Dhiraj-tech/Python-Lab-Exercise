try:
    x=int(input("enter a first num: "))
    y=int(input("enter a second num: "))
    print("The result is: ",x/y)
except BaseException as e:
    print("The type of exception: ",type(e))
    print("The description is: ",e)
    try:
        x
    except NameError:
        x=int(input("enter first num: "))
    try:
        y
    except NameError:
        y=int(input("enter a second num: "))
    print("The result is: ",x/y)
