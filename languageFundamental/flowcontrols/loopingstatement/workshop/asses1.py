#print true if sum of two numbers is 100,and print true if one of them equals 100
num1=int(input("Enter No.1 "))
num2=int(input("Enter No.2 "))
if ((num1+num2==100)|(num1==100)|(num2==100)):
    print("True")
else:
    print("False")