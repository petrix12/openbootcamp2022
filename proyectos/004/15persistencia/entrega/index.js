let nombre = "Pedro"
let apellido = "Bazó"
let persona = {
    nombre,
    apellido
}

sessionStorage.setItem("persona", JSON.stringify(persona))
localStorage.setItem("persona", JSON.stringify(persona))

const now = new Date()
`persona=${JSON.stringify(persona)};expires=${new Date(now.getTime() + 2 * 60000)}`