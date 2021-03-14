class Calc{
    add(){
        console.log("no argumnent methode");
    }
    add(num){
        console.log("one arguments");
    }
    add(num1,num2){
        console.log("two args");
    }
}
// methode overloading ::: same class name but different number of arguments

var cal=new Calc();
cal.add(10,20)
cal.add(10)

// it works recently added methode