class A:
    def area(self):
        r=5
        a=22/7*(r**2)
        print("area of circle:",a)
class B(A):
    def rect(self):
        l=5
        b=10
        a=l*b
        print("area of rectangle:",a)
class C(B):
    pass
obj=C()
obj.area()
obj.rect()
