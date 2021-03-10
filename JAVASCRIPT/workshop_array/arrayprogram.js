// var numbers=[12,54,78,76,89,43]
// for(let num of numbers){
//     console.log(num);
// }

var arr1=[10,30,34,56,76]
var arr2=[11,21,30,34,50]
var pos1=0
var pos2=0
var common=[]
// for(let i of arr1){
//     for(let j of arr2){
//         if(i==j){
//             console.log(i);
//         }
//     }
// }
if(pos1<arr1.length){
    if(pos2<arr2.length){
        if(arr1[pos1]==arr2[pos2]){
            common.push((arr1[pos1],arr2[pos2]));
            pos1+=1
            pos2+=1
        }
        else if(arr1[pos1]>arr2[pos2]){
            pos2+=1
        }
        else if(arr1[pos1]<arr2[pos2]){
            pos1+=1
        }
    }
}
console.log(common);