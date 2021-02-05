class parent:
    def m1(self):
        print("Parent")

class child(parent):
    def m2(self):
        print("Child")
class subchild(child):
    def m3(self):
        print("Subchild")

obj=subchild()
obj.m3()
obj.m2()
obj.m1()