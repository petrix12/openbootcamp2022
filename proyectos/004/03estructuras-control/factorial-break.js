numero = 10
factorial = 1

let i = 1
while(true) {
    factorial *= i
    i++
    if(i > numero) {
        break
    }
}

console.log(`El factorial de ${numero} es ${factorial}`)