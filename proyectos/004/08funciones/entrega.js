// Parte I: Una función sin parámetros que devuelva siempre "true"
const cierto = () => true

// Parte II: Una función asíncrona que utilice un setTimeout y pase por consola un "Hola soy una promesa" 5 segundos después de haberse ejecutado
const funcionAsync = new Promise((resolve, reject) => {
    if (true) {
        setTimeout(() => console.log("Hola soy una promesa"), 5000)
    } else {
        reject()
    }
})

// Parte III: Una función generadora de índices pares automáticos
function* generaId() {
    let id = 0;
    while(true) {
        id += 2
        yield id
    }
}

const gen = generaId();

console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)