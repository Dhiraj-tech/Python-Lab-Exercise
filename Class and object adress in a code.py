class Abc:
    def xyz(self,x):
        print(self)
        print(x)
    @classmethod
    def class_xyz(cls,x):
        print(cls)
        print(x)
    @staticmethod
    def static_xyz(x):
        print(x)
obj=Abc()
obj.xyz(5)
obj.class_xyz(5)
obj.static_xyz(5)
