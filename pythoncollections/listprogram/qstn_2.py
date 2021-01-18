lst=[1,2,3,5]
lst.sort()
num=int(input("Enter the sum that u want : "))
low=0
upp=len(lst)-1
while(low<upp):
    tot=lst[low]+lst[upp]
    if(tot==num):
        print(lst[low],lst[upp])
        break
    else:
        low+=1



