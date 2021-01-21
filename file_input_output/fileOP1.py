#read
#write
#append



#step1 : we have to create a refference
# f=open("filepath","mode"     r-reading    w-writing    a-append

f=open("demo","r")
word=[]

for line in f:
    word.append(line.rstrip("\n")split(" "))
print(word)
myword=[]
