class Employee{
    constructor(eid,name,salary,desig){
        this.eid=eid
        this.name=name
        this.salary=salary
        this.desig=desig
    }
    printdetails=()=>{
        console.log(this.eid+this.name+this.salary+this.desig);
    }
}
var employee=[]
var obj1=new Employee(100,"ajay",25000,"developer");
var obj2=new Employee(101,"vijay",24000,"developer");
var obj3=new Employee(102,"varun",27000,"qa");
var obj4=new Employee(103,"dileep",26000,"qa");
employee.push(obj1)
employee.push(obj2)
employee.push(obj3)
employee.push(obj4)
console.log(employee);


// designation of all employees
employee.forEach(emp=>console.log(emp.desig))

// add 2000 bonus to every employee
employee.map(emp=>emp.salary+2000).forEach(salary=>console.log(salary))


// convert to upper case name of all employee
employee.map(emp=>emp.name.toUpperCase()).forEach(name=>console.log(name))

// employees of  developers
employee.filter(emp=>emp.desig=="developer").forEach(emp=>console.log(emp.name))


// sorting based on salary
console.log("sorted salary list");
employee.map(emp=>emp.salary).sort((sal1,sal2)=>sal2-sal1).forEach(sal=>console.log(sal))

// other solution for sorting
console.log("alter methode");
employee.sort((o1,o2)=>o1.salary>o2.salary?1:-1).forEach(emp=>console.log(emp))

// lowest salary
const sal=employee.map(emp=>emp.salary).reduce((sal1,sal2)=>sal1<sal2?sal1:sal2)
console.log(sal);