lst=[10,11,12,13,14,15,16,17]
lstod=list()
lstev=list()
for num in lst:
    if num%2==0:
        lstev.append(num)
    else:
        lstod.append(num)
print(lstod)
print(lstev)
print("Odd sum is ",sum(lstod))
print("even sum is ",sum(lstev))