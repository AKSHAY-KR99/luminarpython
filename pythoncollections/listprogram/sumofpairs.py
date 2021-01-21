lst=[1,2,3,4,5,6,7,8]
lst.sort()
element=int(input("Enter the sum tht u want "))
low=0
upp=len(lst)-1
pair_lst=list()
while(low<upp):
    tot=lst[low]+lst[upp]
    if(element==tot):
        pair_lst.append((lst[low],lst[upp]))
        upp-=1
    elif(element<tot):
        upp-=1
    elif(element>tot):
        low+=1
print(pair_lst)





