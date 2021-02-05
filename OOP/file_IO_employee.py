# print employee details designation 'developer'
# no of employees as developer
# print employee details who have highest salary

class Employee:
    def __init__(self,eid,name,desig,exp,salary):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name

f=open("employees","r")

emplist=[]
salary_list=[]
for lines in f:
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(eid,name,desig,exp,salary))

# HIGHEST SALARY
for emp in emplist:
    salary_list.append(emp.salary)
print(max(salary_list))


# who gain lowest salry in developer designation
devsalary=[]
for emp in emplist:
    if emp.desig=='developer':
        devsalary.append(emp.salary)
print(devsalary)
minsalary=min(devsalary)
print("min salary:",minsalary)
for emp in emplist:
    if emp.salary==minsalary:
        print(emp.name)

namelst=[]
for emp in emplist:
    namelst.append(emp.name)
print(namelst)
uppname=list(map(lambda line:line.upper(),namelst))
print(uppname)




