print("enter a four subjects mark")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
t=a+b+c+d
print("total marks",t)
per=(t/400)*100
print("total percentage",per)
if per>=70:
    print("distinction")
elif per>=60 and per<70:
    print("first division")
elif per>=40 and per<60:
    print("passs")
else:
    print("fail")
    