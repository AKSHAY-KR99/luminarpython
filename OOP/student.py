class Student:
    def set_Student(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name
    def get_Student(self):
        print("Roll No.:",self.rol,"   Name:",self.name,"   Course:",self.course)


obj1=Student()
obj1.set_Student(1001,"mca","ajay")
obj1.get_Student()


obj2=Student()
obj2.set_Student(1002,"bca","vijay")
obj2.get_Student()

print(obj2.rol)
print(obj1.course)

#set_students
# initilising with instance variables
# instance variable:: variable with 'self' keyword
# we can use instance variable outside the class by reference
# inside the class use 'self' keyword