try:
    x=int(input("enter a first num: "))
    y=int(input("enter a second num: "))
    print("The result is: ",x/y)
except(ZeroDivisionError,ValueError) as ms:
    print("Exception name: ",ms)
    print("plz provide valid input only ",ms)
