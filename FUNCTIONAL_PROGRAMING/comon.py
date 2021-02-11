#comon elements in array
#[1,2,3,4,5,6][4,8,5,1,9,0]
lst1=[1,2,3,4,5,6]
lst2=[4,8,5,1,9,0]
comon=list(filter(lambda num:num in lst1,lst2))
print(comon)

ls3=[2,4,6,4,7,8,4,1,7,9,3]
ls4=[4,6,7,81,76,8]
com1=list(filter(lambda v:v in ls4,ls3))
print(com1)
com2=set(com1)
print(com2)