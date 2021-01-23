f=open("demo","r")
word=[]

for line in f:
    word.append(line.rstrip("\n").split(" "))
print(word)
lst=[]
for i in word:
    for j in i:
        lst.append(j)
print(lst)
dict={}
for ch in lst:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
print(dict)
result=sorted(dict,key=dict.get,reverse=True)
print(result[0],"-is most repeating word")
print(dict[result[0]],"times")