nombre = "Pedro"
apellido = "Bazó"
estudiante = `${nombre} ${apellido}`
estudianteMayus = estudiante.toUpperCase()
estudianteMinus = estudiante.toLowerCase()
letrasEstudiante = estudiante.length
primerLetraNombre = nombre.substring(0,1)
ultimaLetraApellido = apellido.substring(apellido.length - 1, apellido.length)
estudianteSinEspacios = estudiante.replace(/ /g, '')
estaNombreEnEstudiante = estudiante.includes(nombre)

console.log("nombre:", nombre)
console.log("apellido:", apellido)
console.log("estudiante:", estudiante)
console.log("estudianteMayus:", estudianteMayus)
console.log("estudianteMinus:", estudianteMinus)
console.log("letrasEstudiante:", letrasEstudiante)
console.log("primerLetraNombre:", primerLetraNombre)
console.log("ultimaLetraApellido:", ultimaLetraApellido)
console.log("estudianteSinEspacios:", estudianteSinEspacios)
console.log("estaNombreEnEstudiante:", estaNombreEnEstudiante)