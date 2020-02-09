try:
    x=int(input("enter a first num: "))
    y=int(input("enter a second num: "))
    print("The result is: ",x/y)
except ZeroDivisionError:
    print("ZeroDivisionError:divided by zero")
except:
    print("Default except block:provide int values")