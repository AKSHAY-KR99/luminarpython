pattern="ABABBAC"
#find first recursive chctr A
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"is the recursive charecter")
        break