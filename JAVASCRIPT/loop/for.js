
var num=16
var flag=0
for(let i=2;i<num;i++){
    if(num%i==0){
        flag+=1
        break
    }
    flag=0
}
if(flag==0){
    console.log("Prime Number");
}
else{
    console.log("Not prime");
}