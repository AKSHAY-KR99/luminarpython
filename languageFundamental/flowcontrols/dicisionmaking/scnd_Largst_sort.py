num1=int(input("Enter no1 "))
num2=int(input("Enter no2 "))
num3=int(input("Enter no3 "))
if((num1>num2)&(num1>num3)):
    if num2>num3:
        print(num2," is second largest")
        print("Sorted order is ",num1,num2,num3)
    else:
        print(num3," is second largest")
        print("Sorted order is ", num1, num3, num2)
elif((num2>num1)&(num2>num3)):
    if num1>num3:
        print(num1," is second largest")
        print("Sorted order is ",num2,num1,num3)
    else:
        print(num3," is second largest")
        print("Sorted order is ", num2, num3, num1)
elif((num3>num2)&(num3>num1)):
    if num2>num1:
        print(num2," is second largest")
        print("Sorted order is ",num3,num2,num1)
    else:
        print(num1," is second largest")
        print("Sorted order is ", num3, num1, num2)
else:
    print("Numbers are equal")