 var student=[
    [10,"ajay","bca",250],
    [11,"aju","bca",240],
    [12,"jay","bca",220],
    [13,"ashi","bca",220],
    [14,"vijay","mca",180],
    [10,"jain","mca",250]]
//print student details who studying bca
for(let stud of student){
    for(let std of stud){
        if(std=="bca"){
            console.log(stud);
        }
    }
} 
// print average mark from list
var sum=0
for(let i=0;i<student.length;i++){
    sum=sum+student[i][3]
    
}
console.log(sum);
avg=sum/6
console.log("average is "+avg);
