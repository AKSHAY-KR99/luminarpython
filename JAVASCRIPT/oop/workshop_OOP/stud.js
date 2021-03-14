class Student{
    setStudent(roll,name,course,mark){
        this.roll=roll
        this.name=name
        this.course=course
        this.mark=mark
    }
    getStudent(){
        console.log(this.roll+","+this.name+","+this.course+","+this.mark);
    }
}
obj=new Student
obj.setStudent(8,"Fathima Hiba P","medicine",90)
obj.getStudent()
