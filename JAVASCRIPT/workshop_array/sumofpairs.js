arr=[1,2,3,4,5,6,7,8]
var sumlist=[]
var num=5
var low=0
var upp=arr.length-1
while(low<upp){
    tot=arr[low]+arr[upp]
    if(tot==num){
        sumlist.push(arr[low],arr[upp])
        upp-=1
    }
    else if(num<tot){
        upp-=1
    }
    else if(num>tot){
        low+=1
    }
}
console.log(sumlist);

