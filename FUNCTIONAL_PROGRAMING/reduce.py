lst=[11,22,33,44,]
from functools import reduce
sumoflist=reduce(lambda no1,no2:no1+no2,lst)
print(sumoflist)
high=max(lst)
print("Highest:",high)
mxm=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print("Highhhh::",mxm)
