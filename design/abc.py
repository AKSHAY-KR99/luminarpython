def smart_sub(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrapper




@smart_sub
def sub(num1,num2):
    return num1-num2

result=sub(3,5)
print(result)