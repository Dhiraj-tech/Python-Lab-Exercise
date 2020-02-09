#defining a shownumber function upto limit and print 0(even),1(odd) and 2(even)...................
def shownumbers():
    for i in range(10):
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
shownumbers()
