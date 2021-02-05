class parent:
    def m1(self):
        print("Parent")

class child:
    def m1(self):
        print("Child")
class subchild(parent,child):   #it read methodes by order of inputed subchild(1,2,3,4,5,etc):
    def m3(self):
        print("Subchild")

obj=subchild()
obj.m3()
obj.m1()