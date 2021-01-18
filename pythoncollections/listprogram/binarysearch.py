limit=int(input("Enter the limit : "))
lst=list()
for i in range(0,limit):
    num=int(input("Enter value : "))
    lst.append(num)
#first sort the given list
#[5,6,7,8,10,11,12]
# l               u
#mid=(l+u)//2
lst.sort()
print(lst)
low=0
upp=len(lst)-1
flag=0
element=int(input("Enter the element :"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=flag+1
        break
if(flag==0):
    print("Item not found")
else:
    print("Item found")



