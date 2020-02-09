num=(6,2,1,4,3)
x=list(num)
print(x)
x.append(9)
i=0
while i<5:
    j=0
    while j<4:
        if x[j]> x[j+1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
        j=j+1
    i=i+1
print(x)
z=tuple(x)
print(z)
