#input 123 then output will be 321
num=int(input("Enter a number "))
while(num!=0):
    dig=num%10
    print(dig,end="")
    num=num//10