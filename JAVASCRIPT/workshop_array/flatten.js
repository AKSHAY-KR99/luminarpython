lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
lst1=[]
console.log(lst);
for(let i of lst){
    for(let j of i){
        lst1.push(j)
    }
}
console.log(lst1);