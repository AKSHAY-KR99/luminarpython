isl_2=[
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
from functools import reduce

#highest point team

point_high=reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["pts"],isl_2)))
print(point_high)
team_nameh=list(filter(lambda team:team["pts"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["pts"],isl_2))),isl_2))
print(team_nameh)

point_low=reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["pts"],isl_2)))
print(point_low)
team_namel=list(filter(lambda team:team["pts"]==reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["pts"],isl_2))),isl_2))
print(team_namel)