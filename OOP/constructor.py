#CONSTRUCTOR
# duty:: initialising instance variable constructor name always a class name
# in python constuctor is __init__()



class employee():
    def __init__(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def get_employee(self):
        print("ID:",self.id,"  Name:",self.name,"  Designation:",self.designation,"  salary:",self.salary)

obj1=employee(1001,"alex","HR",30000)
obj1.get_employee()

obj2=employee(1002,"David","Manager",50000)
obj2.get_employee()