var emp={
    id:1000,name:"ajay",desig:"developer",salary:25000
}
console.log(emp["name"]);
console.log(emp.name);

// checking for gender is there
console.log("gender" in emp);
emp["gender"]="male"
console.log(emp);
for(let key in emp){
    console.log(key);
}