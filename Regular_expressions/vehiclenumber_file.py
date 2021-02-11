from re import *
f=open("vehiclenumber","r")
valid=[]
invalid=[]
rules='kl\d{2}\w{1,2}\d{4}'
for i in f:
    line=i.rstrip("\n")
    matcher=fullmatch(rules,line)
    if matcher==None:
        invalid.append(line)
    else:
        valid.append(line)
print("Valid Reg No ",valid)
print("Invalid Reg No ",invalid)