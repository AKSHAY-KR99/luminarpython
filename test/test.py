num1=int(input("Enter 1"))
num2=int(input("Enter 2 "))
c=0
for num in range(num1, num2+1):
    for i in range(2, (num//2)+1):
        if (num % i == 0):
            c+=1
            break
        if(c==0):
            print(num)