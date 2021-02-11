from re import *
mail=input("Enter mail id  :")

id="[a-zA-Z.]*[/d]*@gmail.com"

matcher=fullmatch(id,mail)
if matcher==None:
    print("Invalid variable mail.....!!!")
else:
    print(" VALID MAIL ID  ")