student=["name1","name2","name3","name3"]
fail=["name1","name2"]
studset=set(student)
failset=set(fail)
passed=studset.difference(fail)
print("Passed students : ",list(passed))