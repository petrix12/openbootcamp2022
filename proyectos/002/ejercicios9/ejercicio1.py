paisesString = input("Lista de países separados por comas: ")
paises = [pais for pais in paisesString.split(",")]
print("Lista ordenada:", ",".join(sorted(list(set(paises)))))