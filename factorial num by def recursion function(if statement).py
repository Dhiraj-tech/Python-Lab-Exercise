num=int(input("enter a num:"))
def recurfactorial(num):
    if num==1:
        return 1
    else:
        return (num*recurfactorial(num-1))
ans=recurfactorial(num)
print("factorial num is:",ans)
