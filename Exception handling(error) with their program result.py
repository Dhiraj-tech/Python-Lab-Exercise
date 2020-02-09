try:
    x=int(input("enter a first num: "))
    y=int(input("enter a second num: "))
    print("The result is: ",x/y)
except BaseException as e:
    print("The type of exception: ",type(e))
    print("The description is: ",e)
    y=int(input("enter the value for y again: "))
    print("The result is: ",x/y)
