#WAP to take a user input of  number and find the median(median=(n+1)/2)
list=[1,2,3,4,5,6,7,8]
n=len(list)
list.sort()
if n%2==0:
    median1=list[n//2]
    median2=list[(n//2)-1]
    median=(median1+median2)/2
else:
    median=list[n//2]
print("Median:",median)
