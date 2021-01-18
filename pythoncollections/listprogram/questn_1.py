limit=int(input("Enter a limit : "))
lst=list()
for i in range(0,limit):
    number=int(input("Enter Number : "))
    lst.append(number)
print("the given list is ",lst)
total=sum(lst)
out=list()
for num in lst:
    out.append(total-num)
print("The output is ",out)



    