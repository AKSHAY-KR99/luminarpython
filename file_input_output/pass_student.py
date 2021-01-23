total=open("students","r")
fail=open("fail","r")
tot=[]
fl=[]
for name in total:
    tot.append(name.rstrip("\n"))
for name in fail:
    fl.append(name.rstrip("\n"))
print(tot)
print(fl)
set_tot=set(tot)
set_fail=set(fl)
passed=set_tot.difference(set_fail)
print("Passed students are ",passed)
