from  re import *
f=open("phonenumber","r")
rule="(91)?\d{10}"
valid=[]
invalid=[]
for i in f:
    line=i.rstrip("\n")
    matcher=fullmatch(rule,line)
    if matcher==None:
        invalid.append(line)
    else:
        valid.append(line)
print("valid phone numbers ",valid)
print("Invalid phone numbers ",invalid)
