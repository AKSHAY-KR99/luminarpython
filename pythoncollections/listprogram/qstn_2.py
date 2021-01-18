lst=[1,2,3,4,5,6]
num=int(input("Enter the sum that u want : "))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==num:
            print(lst[i],",",lst[j]," ")
        else:
            pass


