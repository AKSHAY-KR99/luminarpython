#comon elements in array
#[1,2,3,4,5,6][4,8,5,1,9,0]
lst1=[1,2,3,4,5,6]
lst2=[4,8,5,1,9,0]
comon=set(lst1).intersection(set(lst2))
print(comon)
