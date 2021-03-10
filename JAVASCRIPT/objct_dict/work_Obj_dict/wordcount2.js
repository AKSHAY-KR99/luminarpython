var text = "Energetic graduate from Calicut University, ability to update and learn new concepts quickly and strong desire to work in Designing field. Wish to work in a highly competitive environment with a perfect challenge by contributing the best for the growth of the organization while ensuring growth in personal career"
var words=text.split(" ")
var dict={}
// console.log(words);
for(let word of words){
    if(word in dict){
        dict[word]+=1
    }
    else{
        dict[word]=1
    }
}
console.log(dict);