

                                ##--CARPETA: EJERCICIOS DEL MODULO I
# PROBLEMA 1: 
# Asegúrese de probar su código para cada uno de los siguientes.

#  - Ejecute su programa como python hello.py y espere a que se le solicite
#    la entrada. Escribe Emmay presiona enter. Su programa debería generar hello, Emma.
#   - Ejecute su programa como python hello.py y espere a que se le solicite la 
#   entrada. Escribe Rodrigoy presiona enter. Su programa debería generar hello, Rodrigo.
a = input("What is your name: ")
print(a)
print("hello", a)

b = input("What is your name: ")
print(b)
print("hello", b)

## PROBLEMA 2:
# Leer llave sustitucion y solicitar plaintext
# * Obtengo una lista con el abecedario
# * Reccoro letra por letra de plaintext, identifico la posición de la 
#   letra en el abecedario y se reemplaza por la posición de la letra en la llave 
#   sustitición
##----FALTA RESOLVER EL CODIGO--






## PROBLEMA DIVERSOS:
## ejercicio 1-
#--Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés 
# al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te
#  añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience 
# leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el
#  usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de 
# ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
cantidad= float(input('Ingrese cantidad de dinero depositada en la cuenta de ahorros:' ))
anio = 0
for anio in range(3):
    anio= anio +1
    interes= 0.04* cantidad
    cantidad = cantidad + interes
    print(round(cantidad,2))

## ejercicio 2:
# Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0)</code> y escriba la solución.
# Se recuerda que una ecuación de segundo grado puede no tener solución, tener 
# una solución única, tener dos soluciones o que todos los números sean solución.
## Su programa debe indicar:
#       - En caso la ecuación cuadrática tenga solución real, su programa debe brindar la solución
#       - En caso su ecuación no tenga solución real, su programa debe brindar un mensaje que diga "Ecuación no presenta solución real"
from math import sqrt
a= int(input('Ingrese un valor diferente a 0: '))
b= int(input('Ingrese el valor de b: '))
c= int(input('Ingrese el valor de c: '))
if a != 0:
    #calculando discrimante
    d= (b**2 - 4*a*c)

    if d<0: 
        print('Ecuación no presenta solución real')
    else: 
        x1= (-b+ sqrt(d))/(2*a)
        x2= (-b- sqrt(d))/(2*a)
        print(f'Los valores son {x1} y {x2}')
else:
    print (f'el valor de a debe ser distinto de cero')

##


