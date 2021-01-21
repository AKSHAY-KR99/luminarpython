expense={"jan20":20000,"feb20":30000,"march20":28000,"april20":25000,"may20":22000}
#values stored in dictionary in the form of KEY work
#fetch value using keyword
#duplicate not possible , immutable
#KEY must be unique
print(type(expense))
print(expense["may20"])

print("june20" in expense)

#adding new key values
#june20=25000
expense["june20"]=25000
print(expense)

#updating
print("march20" in expense)
expense["march20"]+=2000
print(expense["march20"])

