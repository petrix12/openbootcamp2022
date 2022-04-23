class Alumno:
    nombre = None
    nota = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota(self, nota):
        self.nota = int(nota)

    def showResultados(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
        print("APROBADO" if self.nota >= 16 else "REPROBADO")

alumno = Alumno()
alumno.setNombre(input("Nombre: "))
alumno.setNota(input("Nota: "))
alumno.showResultados()

