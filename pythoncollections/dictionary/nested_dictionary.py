employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"john","salary":30000,"exp":2},
    1002:{"id":1002,"name":"danie","salary":35000,"exp":2},
    1003:{"id":1003,"name":"jack","salary":30000,"exp":2},
}
print(employee[1000])

#print employee name whose id is 1001
if 1001 in employee:
    print(employee[1001]["salary"])
else:
    print("ID does not exist")


#name of employee whoes i is 1003

if 1003 in employee:
    print(employee[1003]["name"])
else:
    print("does not exist")



#QSTN: if argued 1001 it will print the corresponding employee name



def print_employee(id=None,prop=None):
    if id in employee:
        print(employee[id][prop])
    else:
        print("ID does not exist")

print_employee(id=1000,prop="exp")


#this methode is not possible when many number of arguments are inputed
#so we use **kwags methode