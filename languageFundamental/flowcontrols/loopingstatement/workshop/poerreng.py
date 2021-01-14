#2
#2+22=24
#3
#3+33+333=369

num=input("Enter a number : ")
data=""
res=0
for i in range(1,int(num)+1):
    data=num*i
    print(data," ",end="")
    res=res+int(data)

print("Sum is ",res)