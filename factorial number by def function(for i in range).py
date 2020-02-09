x= int(input("Enter a number:"))
def function(x):
    fact=1
    for i in range(2,x+1):
        fact=fact*i
    return(fact)
ans=function(x)
print(ans)