// if u entered 3 with in the limit 1 and 100 then print cubes b/w 1 and 100
// if u entered 2 with in the limit 1 and 100 then print squares b/w 1 and 100
// if u entered 5 with in the limit 1 and 100 then print power rise to 5 b/w 1 and 100
num=3
upp=500
low=1
for(i=1;i<=upp;i++){
    if(((num**i)<=upp)&((num**i)>=low)){
        console.log(num**i);
    }
}