#write a function called show numbers that takes a parameter called limit .
#It should print all the numbers between 0 and limit with to identify even and odd and print 0(even),1(odd) and 2(even)
def shownumbers():
    for i in range(100):
        if i==3:
            break
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
shownumbers()
