text="hello hai hello hai hello come on kerala come on blasters"
#word count
#hello:3, hai:2
#movie
#covid
print(text)
words=text.split(" ")
dic={}
for word in words:
    if word not in dic: #word illa,threfor aa word dic ilek add cheythu
        dic[word]=1
    else: #aa word dictil und, so incriment cheythu
        dic[word]+=1
print(dic)