class Estudiante {
    nombre = "Pedro"
    asignaturas = ['Javascript', 'HTML', 'CSS']

    obtenDatos() {
        return {
            nombre: this.nombre,
            asignaturas: this.asignaturas
        }
    }
}

const estudiante = new Estudiante
const datos = estudiante.obtenDatos()
console.log(datos)