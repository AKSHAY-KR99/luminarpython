emp={id:100,name:"ajay",exp:2,salary:25000}
if("salary" in emp){
    console.log(emp.salary);
}
console.log(emp.name);
if("gender" in emp){
    console.log("gender exist");
}
else{
    emp["gender"]="male"
}
console.log(emp);
// if salary less than 30000 then add 3000 more
if(emp.salary<30000){
    emp.salary+=3000
}
else{
    console.log("Salary greater than 30000");
}
console.log(emp);