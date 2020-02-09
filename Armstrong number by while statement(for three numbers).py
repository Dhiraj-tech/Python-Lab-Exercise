num=int(input("enter a number"))
a=num
total=0
while num>0:
    rem=num%10
    total=total+rem**3
    num=num//10
if a==total:
        print("number is armstrong")
else:
        print("number is no armstrong")