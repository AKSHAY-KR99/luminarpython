var arr=[1,2,3,4,5,6,7,8,9]
var arrodd=[]
var arrevn=[]
for(i of arr){
    if(i%2==0){
        arrevn.push(i)
    }
    else{
        arrodd.push(i)
    }
}
console.log(arrevn);
console.log(arrodd);