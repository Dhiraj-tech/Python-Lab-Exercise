#write a program to take a user input of a numbers in a list and find how many times the number repeat(highest mode)
list=[]
a=int(input("enter how many number of elements "))
for i in range(1,a+1):
    b=int(input("enter a element"))
    list.append(b)
k=0
num=int(input("enter the number to be counted"))
for j in list:
    if j==num:
        k=k+1
print("repetition times",num,"appears is",k)