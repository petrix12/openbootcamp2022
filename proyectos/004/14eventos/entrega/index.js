const boton = document.querySelector("#btn")

boton.addEventListener("click", () => {
    alert("click en el botón")
})

$("button").click(function() {
    console.log("Hola, estoy utilizando jQuery")
})