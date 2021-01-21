employee={"id":100,"ename":"ajay","exp":2,"salary":35000}
if "salary" in employee:
    print(employee["salary"])
print(employee["ename"])
if "gender" in employee:
    print("exist")
else:
    print("Not exist")
    employee["gender"]="male"
print(employee)

#if salary < 35000 then icrease salary by 5000
if employee["salary"]<=35000:
    employee["salary"]+=5000
print(employee)