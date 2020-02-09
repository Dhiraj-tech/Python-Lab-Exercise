num=int(input("enter a num :"))
def recur_sum(num):
    if num<=1:
        return num
    else:
        return num+recur_sum(num-1)
ans=recur_sum(num)
print("sum of natural num",ans)
