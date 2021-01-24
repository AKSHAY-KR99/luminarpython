f=open("movies.csv","r")
dict={}
year_dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=int(data[2])
    movie=data[1]
    if movie not in dict:
        dict[movie]=year
    else:
        dict[movie]=year
    for cinema in data:
        if year not in year_dict:
            year_dict[year] = 1
        else:
            year_dict[year] += 1
res=sorted(dict,key=dict.get,reverse=True)
print("Year wise list of Flims ",res)
print(year_dict)
num=list()
yearlist=list()
for k,v in year_dict.items():
    num.append(v)
    yearlist.append(k)
print("highest number os films in ",yearlist[0],"and the count is ",num[0])
