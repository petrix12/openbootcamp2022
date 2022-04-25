w = open('archivo.txt', 'w')
w.write('datos linea 1\n')
w.write('datos linea 2\n')
w.close()

a = open('archivo.txt', 'a')
a.write('datos linea 3\n')
a.write('datos linea 4\n')
a.close()