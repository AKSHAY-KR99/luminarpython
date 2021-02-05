class parent:
    def m1(self):
        print("Parent")

class child:
    def m2(self):
        print("Child")
class subchild(child,parent):
    def m3(self):
        print("Subchild")

obj=subchild()
obj.m3()
obj.m2()
obj.m1()