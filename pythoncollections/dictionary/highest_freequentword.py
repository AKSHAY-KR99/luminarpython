pattern="ABABBACEEEEEE"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
print(dict)
for key,value in dict.items():
    print(key," ",value)
print(dict.get("E"))
result=sorted(dict,key=dict.get,reverse=True)
print(result)