                        ## EJERCICIOS MODULO IV

                    # PROBLEMAS DIVERSOS
    # 1) 1. Ficheros
#Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
# fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
# done n es el número introducido.
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()

    # 2) 
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
# tabla-n.txt con la tabla de multiplicar de ese número, done n es el número
#  introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar 
# un mensaje por pantalla informando de ello.
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try:
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())

    # 3)
# Escribir una función que pida dos números n y m entre 1 y 10, lea el 
# fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre
#  por pantalla la línea m del fichero. Si el fichero no existe debe mostrar
#  un mensaje por pantalla informando de ello.
n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try:
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])

                    
