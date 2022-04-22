def esPrimo(numero):
    bPrimo = True
    for i in range(2, numero // 2 + 1):
        if (numero % i == 0):
            bPrimo = False
            break
    return bPrimo

numero = 15
print("El número", numero, "es primo" if esPrimo(numero) else "no es primo")