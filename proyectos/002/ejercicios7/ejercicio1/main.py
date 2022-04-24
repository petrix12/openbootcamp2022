import operaciones as op

def main():
    a = 12
    b = 7
    res_suma = op.sumar(a, b)
    res_resta = op.restar(a, b)
    res_multiplicacion = op.multiplicar(a, b)
    res_division = op.dividir(a, b)

    print("a = ", a, ", b = ", b)
    print("a + b = ", res_suma)
    print("a - b = ", res_resta)
    print("a * b = ", res_multiplicacion)
    print("a / b = ", res_division)

if __name__ == '__main__':
    main()