num=int(input("Enter a number "))
c=0
for i in range(2,num):
    if(num%i==0):
        c=c+1
    else:
        pass
if(c==0):
    print(num,"is a prime number")
else:
    print(num, "is a not prime number")
