
from re import *
f=open("emailfile","r")

rules='^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$' #"[a-z][a-zA-Z0-9]*@yahoomail.com"
valid=[]
invalid=[]
for i in f:
    line=i.rstrip("\n")
    matcher=fullmatch(rules,line)
    if matcher==None:
        invalid.append(line)
    else:
        valid.append(line)

print("Valid mails are :",valid)
print("invalid mails are : ",invalid)
