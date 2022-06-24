listaCompra = [
    'Aguacate',
    'Queso',
    'Cloro',
    'Limón',
    'Piña'
]

listaCompra.push('Aceite de Girasol')
listaCompra.pop()

listaPeliculas = [
    {
        titulo: "La vida es bella",
        director: "Roberto Benigni",
        fecha: new Date(1997, 11, 20)
    },
    {
        titulo: "Los miserables",
        director: "Bille August",
        fecha: new Date(1998, 4, 1)
    },
    {
        titulo: "Escarlata y negro",
        director: "Jerry London",
        fecha: new Date(1983, 1, 2)
    },
    {
        titulo: "Spiderman sin regreso a casa",
        director: "Jon Watts",
        fecha: new Date(2021, 11, 17)
    }
]

listaPeliculasNuevas = listaPeliculas.filter(obj => obj.fecha >= new Date(2010, 0, 1))

listaDirectores = listaPeliculas.map(obj => obj.director)
listaTitulos = listaPeliculas.map(obj => obj.titulo)
listaDirectoresTitulos = listaDirectores.concat(listaTitulos)
listaDirectoresTitulos2 = [...listaDirectores, ...listaTitulos]

console.log("listaCompra: ", listaCompra)
console.log("listaPeliculas: ", listaPeliculas)
console.log("listaPeliculasNuevas: ", listaPeliculasNuevas)
console.log("listaDirectores: ", listaDirectores)
console.log("listaTitulos: ", listaTitulos)
console.log("listaDirectoresTitulos: ", listaDirectoresTitulos)
console.log("listaDirectoresTitulos2: ", listaDirectoresTitulos2)