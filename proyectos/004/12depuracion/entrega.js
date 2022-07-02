function fibonacci(num) {
    let serie = [1]
    let anterior = 0
    for(let i = 1; i < num; i++) {
        serie = [...serie, anterior + serie[i-1]]
        anterior = serie[i-1]
    }
    return serie
}

const prueba = fibonacci(6)
console.log(prueba)