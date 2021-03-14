class Employee{
    constructor(eid,ename,desig,salary){
        this.eid=eid
        this.ename=ename
        this.desig=desig
        this.salary=salary
    }
    getEmployee(){
        console.log(this.eid+","+this.ename+","+this.desig+","+this.salary);
    }
}
obj1=new Employee(1000,"Adith Sanjeev","Manager",25000)
obj2=new Employee(1001,"Aswin k","sales",21000)
obj1.getEmployee()
obj2.getEmployee()