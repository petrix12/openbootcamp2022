from functools import reduce

def impares(lista):
    return filter(lambda x: x % 2 != 0, lista)

def sumatoria(lista):
    return reduce(lambda a, b: a + b, lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Elementos impares: ", list(impares(lista)))
print("Sumatoria de los elementos impares: ", sumatoria(list(impares(lista))))