var pattern="ABCDBASDE"
var dict={}
for(let ch of pattern){
    // console.log(ch);
    if(ch in dict){
        // console.log(ch+" is recursive");
        // break
        dict[ch]+=1
    }
    else{
        dict[ch]=1
    }
}
console.log(dict);

