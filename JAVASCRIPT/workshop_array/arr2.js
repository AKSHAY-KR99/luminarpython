var arr=[1,2,3,4]
var out=[]
var sum=0
for(let i of arr){
    sum=sum+i
}
console.log(sum);
for(let i of arr){
    out.push(sum-i)
}
console.log(out);