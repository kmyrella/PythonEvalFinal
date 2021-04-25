            

                    ## EJERCICIOS DEL MODULO II
## PROBLEMA 1:
# Ejecute su programa y espere una solicitud de entrada. Escribe y presiona enter.
#  Su programa debería generar la siguiente salida. Asegúrese de que la pirámide esté
#  alineada con la esquina inferior izquierda de su terminal y de que no haya espacios
#  adicionales al final de cada línea.
n = int(input("Ingrese un numero: "))
if n<=8:
    for i in range (n+1):
        espacios = n-i
        print(' '* espacios+'#'* i)
elif n==-1:
    print("entrada no valida")
elif n==0:
    print("no")
else:
    print("numero no permitido")

## PROBLEMA 2:
##Revelación
# --Hay más de una forma de hacer esto, ¡así que aquí tienes solo una!
# --Verifique que el programa se ejecutó con un argumento de línea de comando
# --Repita el argumento proporcionado para asegurarse de que todos los caracteres sean dígitos
# --Convierta ese argumento de la línea de comandos de un stringa unint
# --Solicitar al usuario texto sin formato
# --Itera sobre cada carácter del texto sin formato:
# --Si es una letra mayúscula, gírela, conservando el caso, luego imprima el carácter girado
# --Si es una letra minúscula, gírela, conservando el caso, luego imprima el carácter girado
# --Si no es ninguno, imprima el carácter como está
# --Imprimir una nueva línea
def codifica(texto):
    desplazamiento=6
    cifrado=""
    if texto==texto.upper():
        lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    else:
        lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    for car in texto:
        if car in lista:
            cifrado += lista[(lista.index(car)+desplazamiento%(len(lista)))]
        else:
            cifrado+=car
    print(cifrado)
    return cifrado
def descodifica(texto):
    desplazamiento=6
    descifrado=""
    if texto==texto.upper():
        lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    else:
        lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    for car in texto:
        if car in lista:
            descifrado += lista[(lista.index(car)-desplazamiento%(len(lista)))]
        else:
            descifrado+=car
    print(descifrado)
    return descifrado

if __name__=="__main__":
    cifrado=codifica('hello, world')
    descifrado=descodifica(cifrado)

## PROBLEMAS DIVERSOS:
## 1) Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo y permitir el ingreso de 3 notas. 
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

## 2) Informar el promedio de nota del curso total.
print(alumnos) ##----Primero vemos que alumnos se han guardado
alumnos['kelly']
data_1 = [8, 9, 7]
prom_1 = sum(data_1)/len(data_1)
print(prom_1)

alumnos ['lulu']
data_2 = [9, 9, 8]
prom_2 = sum(data_2)/len(data_2)
print(prom_2)

alumnos['myrella']
data_3 = [8, 6, 4]
prom_3 = sum(data_3)/len(data_3)
print(prom_3)

promedio_general = (prom_1 + prom_2 + prom_3)/c
print("el promedio general del curso es ", promedio_general)

## 3) QUIEN TUVO EL PROMEDIO MAS ALTO

for alumno, notas in alumnos.items():
    p = (alumno,sum(notas)/ len(notas))
    print("%s tiene un promedio del curso de: %f" % (p))
