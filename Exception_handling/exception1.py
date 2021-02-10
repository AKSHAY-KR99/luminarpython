#exception :- if an abnormal condition if occured ina program it will automaticaly terminate
#error
num1=int(input())
num2=int(input())
try:
    res=num1/num2 #if input of num2 is '0'
    print("res=",res)
except Exception as e:
    print(e.args)
    print("exception occure")
print("i have one data base operation")
print("file operation")



#exception handling key words:- try,except,finally

# try====> doubt full code
