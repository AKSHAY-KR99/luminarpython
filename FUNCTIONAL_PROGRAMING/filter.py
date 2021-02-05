lst=[1,2,3,4,5,6]
even=list(filter(lambda num:num%2==0,lst))
print(even)
odd=list(filter(lambda num:num%2==1,lst))
print(odd)