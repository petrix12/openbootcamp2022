# import operaciones
import operaciones as op

def main():
    res1 = op.suma(3, 7)
    operador = op.Operador()
    res2 = operador.multi(5, 12)
    print("Main: ", res1, res2)
    op.nombreModulo()

if __name__ == '__main__':
    main()