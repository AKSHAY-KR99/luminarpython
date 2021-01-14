num1=int(input("Enter first Number "))
num2=int(input("Enter second Number "))
num3=int(input("Enter third Number "))
if((num1>num2)&(num1>num3)):
    print(num1,"is highest")
elif((num2>num1)&(num2>num3)):
    print(num2, "is highest")
elif((num3>num1)&(num3>num2)):
    print(num3, "is highest")
else:
    print("Numbers are equal")