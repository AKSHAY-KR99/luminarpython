class Parent{
    m1(){
        console.log("inside parent class");
    }
}
class Child extends Parent{
    m2(){
        console.log("child");
    }
}
class Subchild extends Child{
    m3(){
        console.log("subchild child");
    }
}
var chld=new Subchild();
chld.m1();
chld.m2();
chld.m3();