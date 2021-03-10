class Parent{
    m1(){
        console.log("insideparent class");
    }
}
class Child extends Parent{
    m2(){
        console.log("child");
    }
}
var chld=new Child();
chld.m1();
chld.m2();