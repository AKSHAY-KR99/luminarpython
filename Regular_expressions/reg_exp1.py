#regular expression:- used for pattern matching

#step1:- import re module

from re import *
pattern="ab"

matcher=finditer(pattern,"ababababbbbbaaababab")

cnt=0
#print(matcher)
for match in matcher:
    print(match.start()) #  .start function print the position of matching elements
    print(match.group()) #  .group function prints matching pstterns
    cnt+=1
print("Counting :",cnt)