student=[
    [10,"ajay","bca",250],
    [11,"aju","bca",240],
    [12,"jay","bca",220],
    [13,"ashi","bca",220],
    [14,"vijay","mca",180],
    [10,"jain","mca",250]]
#calculate total of bca and mca
mtotal,btotal=0,0
for stud in student:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print("BCA sum : ",btotal)
print("MCA sum : ",mtotal)