#define a function and show the multiples of 3 and 5(by using limit)
def function(limit):
    for i in range(limit):
        sum=0
        if i%3==0 or i%5==0:
            sum=sum+i
            print (sum)
a=int(input("enter a limit"))
function(a)