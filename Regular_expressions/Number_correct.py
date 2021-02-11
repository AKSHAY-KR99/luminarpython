from re import *
number_plate=input("Enter the reg number  :")

reg_no="kl\d{2}[A-Z]{1,2}\d{4}"

matcher=fullmatch(reg_no,number_plate)
if matcher==None:
    print("Invalid variable reg_number.....!!!")
else:
    print("****valid reg_no***")