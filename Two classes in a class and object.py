class A:
    def area(self):
        r=5
        a=22/7*(r**2)
        print("area of circle:",a)
class B(A):
    pass
obj=B()
obj.area()
