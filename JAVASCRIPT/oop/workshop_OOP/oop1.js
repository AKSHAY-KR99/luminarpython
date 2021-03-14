class Person{
    setperson(age,name){
        this.age=age
        this.name=name
    }
    printperson(){
        console.log(this.age+","+this.name);
    }
}

obj=new Person
obj.setperson(25,"Sidhin Das")
obj.printperson()
