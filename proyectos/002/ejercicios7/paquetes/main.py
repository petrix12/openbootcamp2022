from operaciones import suma
import operaciones.resta

def main():
    res1 = suma.suma(2, 7)
    res2 = operaciones.resta.resta(12, 7)
    print(res1, res2)

if __name__ == '__main__':
    main()