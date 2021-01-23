
text=open("demo","r")
words=[]
for ltr in text:
    word=ltr.rstrip("\n").split(" ")
    for val in word:
        words.append(val)
print(words)
flat=[]
for i in words:
    for j in i:
        flat.append(j)
print(j)


