
from re import *
number_plate=input("Enter the reg number  :")

reg_no="kl[0-9][0-9][A-ZA-Z][0-9][0-9][0-9][0-9]"

matcher=fullmatch(reg_no,number_plate)
if matcher==None:
    print("Invalid variable reg_number.....!!!")
else::
    print("****valid reg_no***")