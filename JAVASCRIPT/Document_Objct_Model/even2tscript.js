var c=document.querySelector("#c")
c.addEventListener("click",()=>{
    c.textContent="you are clicked succesfully on this button"
    c.style.color="blue"
})

var d=document.querySelector("#d")
d.addEventListener("dblclick",()=>{
    d.textContent="succesfully double clicked"
    d.style.color="green"
})

var m=document.querySelector("#m")
m.addEventListener("mouseover",()=>{
    m.textContent="mouse on text"
    m.style.color="red"
})
m.addEventListener("mouseout",()=>{
    m.textContent="Mouse not on text"
    m.style.color="grey"
})