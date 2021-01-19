employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000]

]
#print number of employees in company

print("Number of employees : ",len(employees))



#print how many sLARY company hase to rise


total_amount=0
for emp in employees:
    total_amount+=emp[3]
print("Total amount : ",total_amount)



#group by designaion wise



d_cnt=0
da_cnt=0
ba_cnt=0
for emp in employees:
    if emp[2]=="dataanalyst":
        da_cnt+=1
    elif emp[2]=="ba":
        ba_cnt+=1
    else:
        d_cnt+=1
print("Number of employees data analyst group : ",da_cnt)
print("Number of employees in developer group : ",d_cnt)
print("Number of employees BA group : ",ba_cnt)



#print highest salaried employee


salary_list=list()
for emp in employees:
    salary_list.append(emp[3])
print("Salary of employees : ",salary_list)
high_salary=max(salary_list)
print("High salary is ",high_salary)
for emp in employees:
    if high_salary==emp[3]:
        print(emp)


#print employees name with lowest salary whose designation is developer
low=min(salary_list)
for emp in employees:
    if (emp[2]=="developer") & (emp[3]==low):
        print("Lowest salaried employee is ",emp)

