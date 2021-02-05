name=["ind","aus","sa","eng","wi","pak","srilanka","auckland","indonesia"]
upplst=list(map(lambda line:line.upper(),name))
print(upplst)

# print contry with A

acntry=list(filter(lambda line:line[0]=='a',name))
print(acntry)
