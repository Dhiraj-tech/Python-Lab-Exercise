s=int(input("enter a number"))
def function (s):
    a=s
    sum=0
    while s>0:
        d=s%10
        sum=sum+d
        s=s//10
    return (sum)
ans=function(s)
print(ans)