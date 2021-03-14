var isl_2020=[
    {team:"mumbai city",mp:16,won:11,draw:3,loss:2,pts:36,gf:24,ga:9,gd:15},
    {team:"atk mohunbagan",mp:15,won:9,draw:3,loss:3,pts:30,gf:20,ga:10,gd:10},
    {team:"hydrabad",mp:16,won:5,draw:8,loss:3,pts:23,gf:20,ga:16,gd:4},
    {team:"north east",mp:16,won:5,draw:8,loss:3,pts:23,gf:21,ga:20,gd:1},
    {team:"fc goa",mp:16,won:5,draw:7,loss:4,pts:22,gf:22,ga:18,gd:4},
    {team:"bangaluru",mp:16,won:4,draw:7,loss:5,pts:19,gf:19,ga:19,gd:0},
    {team:"jemshedpur",mp:16,won:4,draw:6,loss:6,pts:18,gf:15,ga:19,gd:-4},
    {team:"chennain",mp:16,won:3,draw:8,loss:5,pts:17,gf:11,ga:16,gd:-5},
    {team:"sc east bangal",mp:16,won:3,draw:7,loss:6,pts:16,gf:14,ga:21,gd:-7},
    {team:"kerala blasters",mp:16,won:3,draw:6,loss:7,pts:15,gf:20,ga:27,gd:-7},
    {team:"odisha",mp:15,won:1,draw:5,loss:9,pts:8,gf:14,ga:25,gd:-11},
]
isl_2020.map(object=>object.team).forEach(team=>console.log(team))

// matched played 

// isl_2020.sort((obj1,obj2)=>obj)

// highest pts

const mpt=isl_2020.map(obj=>obj.pts).reduce((pt1,pt2)=>pt1>pt2?pt1:pt2)
console.log(mpt);

isl_2020.sort((obj1,obj2)=>obj1.mp>obj2.mp?-1:1).forEach(obj=>console.log(obj.team))

// highest point team and team details
let top=isl_2020.sort((obj1,obj2)=>obj1.mp>obj2.mp?-1:1)[0]
console.log(top);