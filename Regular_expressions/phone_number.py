from re import *
number=input("Enter the Mob. Number :")

mob="\d{10}"

matcher=fullmatch(mob,number)
if matcher==None:
    print("Invalid variable number.....!!!")
else:
    print("****valid no***")