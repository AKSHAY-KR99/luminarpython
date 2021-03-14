// var add=(num1,num2)=>num1+num2
// var sub=(num3,num4)=>num3-num4
// var cube=num=>num**3
// console.log(cube(3));   
var arr=[10,20,30,40,54,7,23,2,90,65,9]
// cube
arr.map((num)=>num**3).forEach(num=>console.log(num))

// square
arr.map((num1)=>num1**2).forEach(num1=>console.log(num1))

// rise to 4
console.log("rise to 4 reslut");
arr.map(num=>num**4).forEach(num=>console.log(num))

// sum of array
// var add=(num1,num2)=>num1+num2
// console.log(add(10,200));

// var min=arr.reduce((num1,num2)=>num1<num2?num1:num2)
// console.log(min);
// var mx=arr.reduce((num1,num2)=>num1>num2?num1:num2)
// console.log(mx);

// extarct even numbers
console.log("even");
arr.filter(num=>num%2==0).forEach(num=>console.log(num))

// odd
console.log("odd");
arr.filter(num=>num%2!=0).forEach(num=>console.log(num))

// sorting of array
console.log("sorted array");
arr.sort((no1,no2)=>no2-no1).forEach(num=>console.log(num))

// reduce
let sum=arr.reduce((num1,num2)=>num1+num2)
console.log(sum);

// lowest value
let low=arr.reduce((num1,num2)=>num1>num2?num2:num1)
console.log(low);
let high=arr.reduce((num1,num2)=>num1<num2?num2:num1)
console.log(high);