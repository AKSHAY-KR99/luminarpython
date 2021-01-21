#total,course add
student={"ad":4377,"name":"Akshay","course":"python Django","mark":95}
print(student["name"])
if "course" in student:
    print(student["course"])
else:
    print("No course studying")
#if mark > 95 print dstiction else first class
if student["mark"]>=95:
    print("Distinction")
else:
    print("First class")
#print attendence, if no attendence add attendence
print("attendence" in student)
student["attendence"]=85
print(student)

#if mark is >95 update with 5 else update with 3
if student["mark"]>=95:
    student["mark"]+=5
else:
    student["mark"]+=3
print(student)