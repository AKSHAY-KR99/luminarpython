#num=2 low=8 up=30 print only squares between limits
#num=3 low=8 up=30 print only cubes between limits
num=int(input("Enter a number : "))
low=int(input("Enter lower limit : "))
upp=int(input("Enter upper limit : "))
for i in range(1,(upp+1)):
    if num**i in range(low,upp):
        print(num**i)
    else:
        pass


