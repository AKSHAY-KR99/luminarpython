num1=int(input("Enter number :"))
num2=int(input("Enter number :"))
try:
    res=num1/num2
    print(res)
except:
    num2 = int(input("Enter number :"))
    try:
        res=num1/num2
        print(res)
    except:
        num2 = int(input("Enter number :"))
        res = num1 / num2
        print(res)
finally: #entu sambavichalum mandarory aayitt wor cheyyanda codes
    print("I ave database transaction")
    print("I have file operation")
