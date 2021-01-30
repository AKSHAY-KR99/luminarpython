employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"john","salary":30000,"exp":2},
    1002:{"id":1002,"name":"danie","salary":35000,"exp":2},
    1003:{"id":1003,"name":"jack","salary":30000,"exp":2},
}

def print_employee(**kwargs):
    print(kwargs) #it will print {'id': 1001, 'prop': 'salary'}
    id=kwargs["id"]
    if id in employee:
       # print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass

    else:
        pass


print_employee(id=1001,prop="salary")