class Student{
    constructor(id,name,course){
        this.id=id
        this.name=name;
        this.course=course;
    }
    printStud(){
        console.log(this.id+","+this.name+","+this.course);
    }
}
var obj=new Student(100,"ajay","django");
obj.printStud();