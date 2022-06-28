hoy = new Date()
nacimiento = new Date(1972, 0, 12)
masTarde = hoy.getTime() > nacimiento.getTime()
diaNacimiento = nacimiento.getDate()
mesNacimiento = nacimiento.getMonth() + 1
anyoNacimiento = nacimiento.getFullYear()

console.log("hoy:", hoy)
console.log("nacimiento:", nacimiento)
console.log("masTarde:", masTarde)
console.log("diaNacimiento:", diaNacimiento)
console.log("mesNacimiento:", mesNacimiento)
console.log("anyoNacimiento:", anyoNacimiento)