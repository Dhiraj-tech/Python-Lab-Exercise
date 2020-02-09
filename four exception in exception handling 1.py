try:
    a=int(input("first Number:"))
    b=int(input("second Number:"))
    print(a/b)
    x=int("five")
    print(x)
    with open("jojorabbit.txt","r") as roy:
        roy.read()
    li=["apple","banana","java"]
    c=li[6]
    print(c)

except(ValueError,FileNotFoundError,IndexError,ZeroDivisionError) as c:
    print("you are dumb")
else:
    print("If you can read this means exception didn't occur")
print("over")
