f="hello welcome to ooty nice to meet you have a nice day"
text=f.split(" ")
console.log(text);
var dict={}
for(let word of text){
    if(word in dict){
        dict[word]+=1
    }
    else{
        dict[word]=1
    }
}
console.log(dict);