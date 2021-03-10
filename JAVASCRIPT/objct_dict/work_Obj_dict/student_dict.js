var student={admno:4377,name:"akshay",total:93}
if("total" in student){
    console.log(student.total);
}
else{
    console.log("NO total exist");
}
if("course" in student){
    console.log(student.course);
}
else{
    student["course"]="django"
}
console.log(student);
if(student.total>90){
    student.total+=5
}
console.log(student);