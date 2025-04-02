#Actividad 1
print("Hola Mundo")

#Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Actividad 3
nombre = input(f"Ingrese su nombre: ")
apellido = input(f"Ingrese su apellido {nombre}: ")
edad = int(input(f"Ingrese su edad {nombre} {apellido}: "))
residencia = input(f"¿Cual es su lugar de residencia {nombre} {apellido}?: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Actividad 4
radio = float(input("ingrese el radio en cm: "))
pi = 3.14159
area = float(pi*radio**2)
permietro = float(2*pi*radio)
print(f"El area es: {area:.2f}cm y su permietro es: {permietro:.2f}")

#Actividad 5
segundos = float(input("Ingrese la cantidad de segundos: "))
hora = segundos * 0.000277778
print(f"Los {segundos:.2f} equivalen a {hora:.2f} horas")

#Actividad 6
numero = int(input("Hola!, ingrese un numero natural: "))
print(f"La tabla del numero {numero} es: ")
for i in range(1, 11):
    resultado = i * numero
    print(f"{numero} X {i} = {resultado}")

    #Actividad 7
numero1 = int(input("Hola!, ingrese el 1er numero que no sea el 0: "))
numero2 = int(input("Hola!, ingrese el 2do numero que no sea el 0: "))
if numero1 == 0 and numero2 == 0:
    print(f"Error, su numero es menor o igual a 0, por favor ingrese otro numero")
elif numero1 !=0 and numero2 !=0:
    print(f"La suma de los 2 numeros ingresado es: {numero1+numero2}")
    print(f"La resta de los 2 numeros ingresado es: {numero1-numero2}")
    print(f"La division de los 2 numeros ingresado es: {numero1/numero2}")
    print(f"La multiplicacion de los 2 numeros ingresado es: {numero1*numero2}")

    #Actividad 8
altura = float(input("Hola!, Ingrese su altura en metros (Ej. 1.60): "))
peso = float(input("Ingrese su peso corporal en kg (Ej. 80.2): "))
masa = peso/(altura)**2
print(f"Su indice de masa corporal es de: {masa:.2f}")

#Actividad 9
temperatura_celcius = float(input("Ingrese la temeratura en °C: "))
temperatura_fahrenheit = 9/5 * temperatura_celcius + 32
print(f"La temeratura en °C es: {temperatura_celcius:.2f} y su equivalente en °F es: {temperatura_fahrenheit:.2f}")

#Actividad 10
numero1 = float(input("Hola! Ingrese el 1er numero: "))
numero2 = float(input("Hola! Ingrese el 2do numero: "))
numero3 = float(input("Hola! Ingrese el 3er numero: "))
promedio = (numero1+numero2+numero3)/3
print(f"El promedio es: {promedio:.2f}")