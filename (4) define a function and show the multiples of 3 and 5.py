#write a function that returns a sum of multiples of 3 and 5 between 0 and limit(parameter)
def function():
    for i in range(21):
        sum=0
        if i%3==0 or i%5==0:
            sum=sum+i
            print (sum)
function()