def div():
        a=int(input("enter a first num: "))
        b=int(input("enter a second num: "))
        print("The result is:", a / b)
        ent()

def ent():
        x=int(input("enter a num: "))
        print("the entered num is", x)
        file()

def file():
         p=open("sts.txt","r")
         print(p.write())
         list()
def list():
         m=[1,2,3]
         o=int(input("indexing"))
         print(m[o])
try:
    div()
    ent()
    file()
    list()

except ZeroDivisionError:
    print("cannot divided by zero")
    ent()
    file()
    list()
except ValueError:
    print(" uentered string;sorry")
    file()
    list()
    div()
except FileNotFoundError:
    print("file dont exist")
    list()
    ent()
    div()
except IndexError:
    print("there is no such type of index")
    int()
    div()
    file()
print("boy")
