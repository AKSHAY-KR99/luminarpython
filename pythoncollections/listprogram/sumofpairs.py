lst=[1,2,3,5]
lst.sort()
element=int(input("Enter the sum tht u want "))
low=0
upp=len(lst)-1
while(low<upp):
    tot=lst[low]+lst[upp]
    if(element==tot):
        print("pairs are ",lst[low],lst[upp])
        break
    elif(element<tot):
        upp-=1
    elif(element>tot):
        low+=1

