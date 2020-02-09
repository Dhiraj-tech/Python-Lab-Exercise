#(7) write a program that accepts a string and calculate the number of upper and lower case letter
string="DhiRaj"
count1=0
count2=0
for i in string:
    if (i==i.upper()):
        count1=count1+1
    elif (i==i.lower()):
        count2=count2+1
print("number of upper case letter:",count1)
print("number of lower case letter",count2)
