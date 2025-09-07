#EJ 1
for i in range(0,101):
    print(i)

#EJ 2
numero = int(input("Ingresa un numero entero: "))

digitos = len(str(abs(numero))) 

print("El nro tiene", digitos, "digitos")

#EJ 3
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))

menor = min(a, b)
mayor = max(a, b)

suma = 0
for i in range(menor + 1, mayor):
    suma += i

print(f"La suma de los enteros entre {a} y {b}, excluyendo ambos, es: {suma}")

#EJ 4
suma = 0 
while True:
    numero = int(input("Ingresa un numero entero (0 para terminar): "))
    
    if numero == 0:   
        break
    
    suma += numero 

print("La suma total es:", suma)

#EJ 5
import random

secreto = random.randint(0, 9)

intentos = 0
adivinado = False

print("Ingresar un numero entre 0 y 9 para adivinar cual es:")

while not adivinado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento < secreto:
        print("El número es mayor.")
    elif intento > secreto:
        print("El número es menor.")
    else:
        adivinado = True
        print(f"¡Acertaste! El número era {secreto}. Lo lograste en {intentos} intentos.")

#EJ 6
for i in range(100, -1, -2): 
    print(i)

#EJ 7
n = int(input("Ingresa un numero entero positivo: "))

suma = 0

for i in range(1, n + 1):  
    suma += i

print(f"La suma de los numeros entre 0 y {n} es: {suma}")

#EJ 8
valores = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(valores):
    num = int(input(f"Ingrese el numero {i+1}: "))
    
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Resultados:")
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

#EJ 9
cantidad = 100  

suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / cantidad

print(f"La media de los {cantidad} números ingresados es: {media}")

#EJ 10
numero = int(input("Ingresa un numero entero: "))

numero_invertido = int(str(numero)[::-1])

print("Numero invertido:", numero_invertido)