                            ##EJERCICOS MODULO III
    # PROBLEMA 1:
#En credit.py escribir un programa que solicita al usuario un número de 
# tarjeta de crédito y luego informes (a través de print) si se trata de 
# una válida American Express, MasterCard, o número de tarjeta Visa

def tarjeta_val(N):
    T=""; par=0; impar=0;X=""
    if not N.isdigit():return 1,""
    if len(N)<14 or len(N)>19:return 2,""

    for c in range (0,len(N),2):
            X=str(int(N[c])*2)
            if len(X)==2:
                par+=(int(X[0])+int(X[1]))
            else:par+=int(X)
    for c in range(1,len(N),2):
            impar+=int(N[c])
    if (par+impar)%10!=0:return 3,""
    if int(N[0:2])>49 and int(N[0:2])<56:T="MASTERCARD"
    if N[0:2]=="34" or N[0:2]=="37":T="AMERICAN EXPRESS"
    if N[0]=="4":T="VISA"

    return 4,T

msg=(0,"")

while msg[0]!=4:
    msg=tarjeta_val(input("Ingresa el numero de la tarjeta de credito 13-19: "))
    if msg[0]==1:print("solo numeros del 0 al 9")
    if msg[0]==2:print("Número de tarjeta inválida")
    if msg[0]==3:print("Deben ser mayor a 13 o más y menor o igual de 19 digitos")

print("Esta Tarjeta es Válida!!")
print("Tipo:"+msg[1])

    # PROBLEMA DIVERSOS
#1) Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo y permitir el ingreso de 3 notas. 
# Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.
alumnos = {}
c = int(input("¿cuantos alumnos desea ingresar?:"))
for num in range(c):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Ingrese una nota del alumno comprendida de 0 a 10 (ingrese un numero negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Ingrese una nota del alumno compredida de 0 a 10 (ingrese un numero negativo para terminar):"))
        alumnos[alumno] = notas.copy()
print(alumnos)

## 2) Informar le promedio total del curso
alumnos['kelly']
data_1 = [8,7 , 6]
prom_1 = sum(data_1)/len(data_1)
print(prom_1)

alumnos ['ricardo']
data_2 = [6, 5, 4]
prom_2 = sum(data_2)/len(data_2)
print(prom_2)

promedio_general = (prom_1 + prom_2 )/c
print("el promedio general del curso es ", promedio_general)

#3) Realizar una función que indique quién tuvo el promedio más alto y quién tuvo la nota promedio más baja.
for alumno, notas in alumnos.items():
    p = (alumno,sum(notas)/ len(notas))
    print("%s tiene un promedio del curso de: %f" % (p))

    


