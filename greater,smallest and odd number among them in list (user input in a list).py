#WAP to take a user input of a list consist of ten numbers and find (1)greater no among the list (2)smaller no among the list (3) list of a odd number
list=[]
odd=0
for i in range(10):
    num=int(input("enter a number"))
    list.append(num)
print("minimum no among them:",min(list))
print("maximum no among them:",max(list))
odd=[num for num in list  if num%2==1]
print("odd no among them is:",odd)