## EJ1
edad = int(input("Ingresar edad "))

if edad > 18: 
    print("El usuario es mayor de edad")
else:
    print("El usuario no es mayor de edad")


## EJ2
nota = int(input("Ingrese la nota "))

if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")

## EJ3 
numero = float(input("Ingrese un valor "))

if numero % 2==0: 
    print("Numero par")
else: 
    print("Numero impar")

## EJ4 
edad = int(input("Ingrese su edad"))

if edad < 12:
    print("Es un niño")
elif edad >= 12 and edad < 18:
    print("Es adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto joven")
else: 
    print("Es adulto")

## EJ5
contrasena = input("Ingrese una contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Contraseña correcta")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")

## EJ6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media: " + str(media))
print("Mediana: " + str(mediana))
print("Moda: " + str(moda))

if media > mediana and mediana > moda:
    print("La distribucion tiene un sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("La distribucion tiene un sesgo negativo o a la izquierda")
else:
    print("La distribucion no tiene un sesgo")

## EJ7
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    print(frase + "!")
else:
    print(frase)

## EJ8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (mayuscula), 2 (minuscula) o 3 (inicial mayuscula): "))

if opcion == 1:
    nombre_modificado = nombre.upper()
    print(nombre_modificado)
elif opcion == 2:
    nombre_modificado = nombre.lower()
    print(nombre_modificado)
elif opcion == 3:
    nombre_modificado = nombre.title()
    print(nombre_modificado)
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3")

## EJ9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

## EJ10
hemisferio = input("¿En que hemisferio se encuentra? (N/S): ").upper()
mes = input("¿Que mes es?: ").lower()
dia = int(input("¿Que dia es?: "))

if mes == "diciembre":
    num_mes = 12
elif mes == "enero":
    num_mes = 1
elif mes == "febrero":
    num_mes = 2
elif mes == "marzo":
    num_mes = 3
elif mes == "abril":
    num_mes = 4
elif mes == "mayo":
    num_mes = 5
elif mes == "junio":
    num_mes = 6
elif mes == "julio":
    num_mes = 7
elif mes == "agosto":
    num_mes = 8
elif mes == "septiembre":
    num_mes = 9
elif mes == "octubre":
    num_mes = 10
elif mes == "noviembre":
    num_mes = 11

if hemisferio == "N":
    if (num_mes == 12 and dia >= 21) or (num_mes >= 1 and num_mes <= 2) or (num_mes == 3 and dia <= 20):
        print("Es invierno.")
    elif (num_mes == 3 and dia >= 21) or (num_mes >= 4 and num_mes <= 5) or (num_mes == 6 and dia <= 20):
        print("Es primavera.")
    elif (num_mes == 6 and dia >= 21) or (num_mes >= 7 and num_mes <= 8) or (num_mes == 9 and dia <= 20):
        print("Es verano.")
    else:  
        print("Es otoño.")
elif hemisferio == "S":
    if (num_mes == 12 and dia >= 21) or (num_mes >= 1 and num_mes <= 2) or (num_mes == 3 and dia <= 20):
        print("Es verano.")
    elif (num_mes == 3 and dia >= 21) or (num_mes >= 4 and num_mes <= 5) or (num_mes == 6 and dia <= 20):
        print("Es otoño.")
    elif (num_mes == 6 and dia >= 21) or (num_mes >= 7 and num_mes <= 8) or (num_mes == 9 and dia <= 20):
        print("Es invierno.")
    else: 
        print("Es primavera.")
else:
    print("Hemisferio no valido. Por favor, ingrese 'N' o 'S'.")