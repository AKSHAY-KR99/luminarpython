lst=[10,20,30]
pos=int(input("Enter the position of element :"))
num1=int(input())
num2=int(input())
try:
    res=num1/num2
    print(res)
    print(lst[pos])
except Exception as e:
    print(e.args)