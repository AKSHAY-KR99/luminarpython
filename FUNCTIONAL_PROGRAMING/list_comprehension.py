lst=[1,2,3,4,5,6]

square=[num**2 for num in lst]
print(square)

lst2=[[10,20],[30,40],[50,60]]
flat=[num for lt in lst2 for num in lt]
print(flat)
