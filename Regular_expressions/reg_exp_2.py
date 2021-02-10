from re import *

pattern='[ab]' # to print either a or b
pattern2="[a-z]" #to print small letter a to z
pattern3='[A-Z]' # to print capital A to Z
pattern3="[a-zA-Z]" #print all upper case and lower case latters

matcher=finditer(pattern,"abc _7Z@Kc")
for match in matcher:
    print(match.start())
    print(match.group())
matcher=finditer(pattern2,"abc n __vcb")
for match in matcher:
    print(match.start())
    print(match.group())

matcher=finditer(pattern3,"abc n __vcb")
for match in matcher:
    print(match.start())
    print(match.group())

pattern4='[0,9]' #check for 0 to 9
pattern5="[^0-9]" # except 0 to nine
pattern6="[a-zA-z0-9]" #all words , not read special charector
pattern7="[^a-zA-z0-9]" #all charector