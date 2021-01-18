lst=[10,8,7,11,12,6,5]
#first sort the given list
#[5,6,7,8,10,11,12]
# l               u
#mid=(l+u)//2
lst.sort()
low=0
upp=len(lst)-1
element=int(input("Enter the element :"))
while(low<upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=flag+1




