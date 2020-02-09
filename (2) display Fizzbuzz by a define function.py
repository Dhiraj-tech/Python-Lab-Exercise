def fizz_buzz():
    a=int(input("enter a number"))
    b=a%3
    c=a%5
    if b==0 and c==0:
        print("Fizzbuzz")
    elif b==0:
        print("Fizz")
    elif c==0:
        print("Buzz")
    else:
        print(a)
fizz_buzz()
