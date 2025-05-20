#Actividad 1
for i in range(0,102,2):
    print(i, end=" ")

#Actividad 2
numero_entero = int(input("Ingrese un numero entero: "))
i = 0
while numero_entero > 0:
    i += 1
    numero_entero //= 10
    
print (f"El numero tiene {i} digintos")

#Actividad 3
n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))
suma = 0
if n1 >= n2:
    print("El primer numero debe ser menor que el segundo, por favor ingrese otro numero")             
else:
    for i in range(n1, n2+1):
        suma += i
    print(f"La suma de los numeros entre {n1} y {n2} es: {suma}") 

#Actividad 4
corte = 0
while True:
    numero = int(input("Ingrese un número entero (ingrese 0 para detenerse): "))
    if numero == 0:
        break
    corte += numero

print(f"El total acumulado es: {corte}")

#Actividad 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0

print("Adivina el número secreto entre 0 y 9")

while True:
    intento = int(input("Introduce tu número: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")

#Actividad 6
for i in range(100, -1, -2):
    print(i, end=" ")

#Actividad 7
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(0, numero + 1):
        suma += i
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")

#Actividad 8
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#Actividad 9
import statistics
cantidad = 100

numeros = []

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

media = statistics.mean(numeros)
print(f"La media de los {cantidad} números ingresados es: {media}")

#Actividad 10 
numero = input("Ingrese un número entero: ")
numero_invertido = ''.join(reversed(numero))
print(f"El número invertido es: {numero_invertido}")