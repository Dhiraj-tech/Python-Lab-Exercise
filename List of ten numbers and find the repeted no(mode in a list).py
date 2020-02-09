#write a program to take a user input of Ten numbers in a list and find how many times the number repeat(highest mode)
list=[1,2,1,1,4,1,6,8,1,0]
x=1
def count(list,x):
    count=0
    for num in list:
        if (num==x):
            count=count+1
    return count
print("{} has occured {} times ".format(x,count(list,x)))