#id,name,designation, salary
class employee():
    def set_employee(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def get_employee(self):
        print("ID:",self.id,"  Name:",self.name,"  Designation:",self.designation,"  salary:",self.salary)

obj1=employee()
obj1.set_employee(1001,"alex","HR",30000)
obj1.get_employee()

obj2=employee()
obj2.set_employee(1002,"david","manager",50000)
obj2.get_employee()


print(obj2.salary)
print(obj1.name)