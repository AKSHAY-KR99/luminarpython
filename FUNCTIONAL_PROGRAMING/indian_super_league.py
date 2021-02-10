isl=[
    {"team":"mumbai city","mp":16,"won":11,"draw":3,"loss":2,"pts":36,"gf":24,"ga":9,"gd":15},
    {"team":"atk mohunbagan","mp":15,"won":9,"draw":3,"loss":3,"pts":30,"gf":20,"ga":10,"gd":10},
    {"team":"hydrabad","mp":16,"won":5,"draw":8,"loss":3,"pts":23,"gf":20,"ga":16,"gd":4},
    {"team":"north east","mp":16,"won":5,"draw":8,"loss":3,"pts":23,"gf":21,"ga":20,"gd":1},
    {"team":"fc goa","mp":16,"won":5,"draw":7,"loss":4,"pts":22,"gf":22,"ga":18,"gd":4},
    {"team":"bangaluru","mp":16,"won":4,"draw":7,"loss":5,"pts":19,"gf":19,"ga":19,"gd":0},
    {"team":"jemshedpur","mp":16,"won":4,"draw":6,"loss":6,"pts":18,"gf":15,"ga":19,"gd":-4},
    {"team":"chennain","mp":16,"won":3,"draw":8,"loss":5,"pts":17,"gf":11,"ga":16,"gd":-5},
    {"team":"sc east bangal","mp":16,"won":3,"draw":7,"loss":6,"pts":16,"gf":14,"ga":21,"gd":-7},
    {"team":"kerala blasters","mp":16,"won":3,"draw":6,"loss":7,"pts":15,"gf":20,"ga":27,"gd":-7},
    {"team":"odisha","mp":15,"won":1,"draw":5,"loss":9,"pts":8,"gf":14,"ga":25,"gd":-11},
]
point=[]
from functools import *
#for team in isl:
 #   print(team)

#print team name who has highest point

for team in isl:
    point.append(team["pts"])
#print(point)
highest=reduce(lambda n1,n2:n1 if n1>n2 else n2,point)
lowest=reduce(lambda n1,n2:n1 if n1<n2 else n2,point)
for team in isl:
    if team["pts"]==highest:
        print("Highest point team is ",team["team"])
    elif team["pts"]==lowest:
        print("Lowest pointed team :",team["team"])
    else:
        pass



#which team more goal conceded
coneded_goal=[]
for team in isl:
    coneded_goal.append(team["ga"])
top=reduce(lambda n1,n2:n1 if n1>n2 else n2,coneded_goal)
bottom=reduce(lambda n1,n2:n1 if n1<n2 else n2,coneded_goal)
for team in isl:
    if team["ga"]==top:
        print("Most goal coceded team is ",team["team"],"(",top,")")
    elif team["ga"]==bottom:
        print("Less goal coceded team is ", team["team"], "(",bottom, ")")
    else:
        pass

#total number of goals in isl
goals=[]
for team in isl:
    goals.append(team["gf"])
goal=reduce(lambda n1,n2:n1+n2,goals)
print("Total goals in ISL :",goal)

#print team name who score more than 15 goals
teams=[]
for team in isl:
    if team["gf"]>=15:
        teams.append(team['team'])
print("the team who score more than 15 goals",teams)

#conced less than 15 goals
cnced=[]
for team in isl:
    if team["ga"]<=18:
        cnced.append(team['team'])
print("the team who conced less than 15 goals",cnced)