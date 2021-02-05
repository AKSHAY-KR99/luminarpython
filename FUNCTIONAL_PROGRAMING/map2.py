lst=[1,2,3,4,5,6]
# if num<5 -1 else +1

result=list(map(lambda num: num-1 if num<5 else num+1,lst))
print(result)
numlist=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(numlist)