# Actividad 1
edad = int(input(f"Ingrese su edad: "))
if edad >= 18:
        print(f"Es mayor de edad")
else: print("Es menor de edad")

# Actividad 2
nota = float(input(f"Ingrese su nota: "))
if nota >= 6:
    print(f"Aprobado")
else: print("Desaprobado")

# Actividad 3
numero = int(input(f"Ingrese un numero"))
if numero%2==0:
    print(f"Ha ingresado un número par")
else: print(f"Por favor, ingrese un número par")

# Actividad 4
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Es Niño/a")
elif edad >= 12 and edad < 18:
    print("Es Adolecente")
elif edad >= 18 and edad < 30:
    print("Es Adulto/a joven")
elif edad >= 30:
    print("Es Adulto/a")

# Actividad 5
contraseña = input("Ingrese una contraseña:")
if len(contraseña) >=8 and len(contraseña) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6
import random
numeros_alternativos = [random.randint(1,100) for i in range(50)]
print(f"Los numeros alternativos son: {numeros_alternativos}")
#moda mediana y media
from statistics import mode, median, mean
print(f"La moda es {mode(numeros_alternativos)}")
print(f"La mediana es {median(numeros_alternativos)}")
print(f"La media es {mean(numeros_alternativos)}")
if mean(numeros_alternativos) > median(numeros_alternativos) and median(numeros_alternativos) > mode(numeros_alternativos):
    print("El Sesgo es positivo")
elif mean(numeros_alternativos) < median(numeros_alternativos) and median(numeros_alternativos) < mode(numeros_alternativos):
    print("El Sesgo es negativo")
elif mean(numeros_alternativos) == median(numeros_alternativos) == mode(numeros_alternativos):
    print("Sin sesgo")
else: print("Intente de nuevo")

#Actividad 7
frase = input("Ingrese una frase o palabra: ").lower()
if frase[len(frase)-1] == "a" or frase[len(frase)-1] == "e" or frase[len(frase)-1] == "i" or frase[len(frase)-1] == "o" or frase[len(frase)-1] == "u":
    print(f"{frase}!")
else: print(frase)

#Actividad 8
nombre = input("Ingrese su nombre: ")
opcion = input("Elige una opcion\n1. Mayúsculas\n2. Minuscula\n3. Primera letra mayúscula\n Opcion:")
if opcion == "1":
    nombre_usuario = nombre.upper()
elif opcion == "2":
    nombre_usuario = nombre.lower()
elif opcion == "3":
    nombre_usuario = nombre.title()
else: 
    nombre_usuario = "Por favor, elija una de las opciones indicadas"
print(nombre_usuario)

#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
else:
    print("Error")

#Actividad 10
hemisferio = input("Ingrese el hemisferio donde se encuentra (Norte: N) o (Sur: S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese un día (1-31): "))
if (hemisferio == "N" and ((mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20))):
    estacion = "invierno"
elif (hemisferio == "S" and ((mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20))):
    estacion = "verano"
elif (hemisferio == "N" and ((mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia < 21))):
    estacion = "primavera"
elif (hemisferio == "S" and ((mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia < 21))):
    estacion = "otoño"
elif (hemisferio == "N" and ((mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 21))):
    estacion = "verano"
elif (hemisferio == "S" and ((mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 21))):
    estacion = "invierno"
elif (hemisferio == "N" and ((mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia < 21))):
    estacion = "otoño"
elif (hemisferio == "S" and ((mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia < 21))):
    estacion = "primavera"
else:
    estacion = "una fecha no válida, reintentar"
print(f"Usted se encuentra en {estacion}.")

