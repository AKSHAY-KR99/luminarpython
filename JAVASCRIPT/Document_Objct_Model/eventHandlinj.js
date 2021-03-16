var clk=document.querySelector("#clk")

clk.addEventListener("click",()=>{
    clk.textContent="Clicked";
    clk.style.color="Blue"
})


var dbl=document.querySelector("#dbl")

dbl.addEventListener("dblclick",()=>{
    dbl.textContent="Double Clicked";
    dbl.style.color="GREEN"
})

var mo=document.querySelector("#mo")
mo.addEventListener("mouseover",()=>{
    mo.textContent="mouse over me";
    mo.style.color="skyblue"
})

mo.addEventListener("mouseout",()=>{
    mo.textContent="mouse not over me";
    mo.style.color="violet"
})