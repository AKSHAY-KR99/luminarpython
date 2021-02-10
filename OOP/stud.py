class stud:
    def __init__(self,admno,name,course,mark):
        self.admno=admno
        self.name=name
        self.course=course
        self.mark=mark
    def __str__(self):
            return self.name

obj1=stud(1000,"akshay","django",140)
obj2=stud(1001,"babu","mean",140)
obj3=stud(1002,"hamsa","django",140)

slst=list()
slst.append(obj1)
slst.append(obj2)
slst.append(obj3)
total=0


for stud in slst:
    if stud.course=="django":
        print(stud.name)

        # total mark of DJANGO students

for stud in slst:
    if stud.course=='django':
        total+=stud.mark
print(total)




