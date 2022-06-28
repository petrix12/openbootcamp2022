datos = {
    nombre: "Pedro",
    apellido: "Bazó",
    edad: 50,
    altura: 1.82, 
    eresDesarrollador: true
}
console.log("datos: ", datos)

let { edad } = datos
console.log("edad: ", edad)

datos2 = {
    nombre: "Leticia",
    apellido: "Rodríguez",
    edad: 44,
    altura: 1.63, 
    eresDesarrollador: false
}
console.log("datos2: ", datos2)

datos3 = {
    nombre: "Isabel",
    apellido: "Bazó",
    edad: 20,
    altura: 1.60, 
    eresDesarrollador: false
}
console.log("datos3: ", datos3)

let lista = [datos, datos2, datos3]
console.log("lista: ", lista)

const listaNueva = [ ...lista ]
console.log("listaNueva: ", listaNueva)
listaNueva.sort((a, b) => b.edad - a.edad)
console.log("listaNueva: ", listaNueva)