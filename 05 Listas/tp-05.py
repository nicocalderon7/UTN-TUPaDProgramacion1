## EJ 1
notas = []

for i in range(10):
    nota = int(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)  


print("Notas ingresadas:", notas)


promedio = sum(notas) / len(notas)
print("El promedio es:", promedio)


nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print("La nota más alta es:", nota_mas_alta)
print("La nota más baja es:", nota_mas_baja)

## EJ 2
productos = []

for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)


print("Lista ordenada alfabéticamente:", sorted(productos))


eliminar = input("Ingrese el producto que desea eliminar: ")


if eliminar in productos:
    productos.remove(eliminar)  
    print("Producto eliminado con éxito.")
else:
    print("Ese producto no está en la lista.")

print("Lista actualizada:", productos)

## EJ 3
import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista completa:", numeros)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Lista de pares:", pares)
print("Lista de impares:", impares)

print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

## EJ 4
nros = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repetidos = []
for n in nros:
    if n not in sin_repetidos:
        sin_repetidos.append(n)

print("Lista sin repetidos:", sin_repetidos)

## EJ 5
estudiantes = ["Ana", "Juan", "Pedro", "Lucía", "Sofía", "Diego", "María", "Tomás"]

print("Lista inicial:", estudiantes)

accion = input("¿Queres agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"{nuevo} fue agregado a la lista.")

elif accion == "eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
        print(f"{borrar} fue eliminado de la lista.")
    else:
        print("Ese estudiante no está en la lista.")

else:
    print("Opción no válida.")

print("Lista final de estudiantes:", estudiantes)

## EJ 6
numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)

ultimo = numeros.pop()      
numeros.insert(0, ultimo)   

print("Lista rotada:", numeros)

## EJ 7
temperaturas = [
    [12, 24],  # Día 1
    [15, 28],  # Día 2
    [10, 20],  # Día 3
    [14, 25],  # Día 4
    [13, 27],  # Día 5
    [11, 22],  # Día 6
    [16, 30]   # Día 7
]

minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print("Promedio de mínimas:", promedio_min)
print("Promedio de máximas:", promedio_max)

amplitudes = [dia[1] - dia[0] for dia in temperaturas]

mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1  

print("Mayor amplitud térmica:", mayor_amplitud)
print("Se registró en el día:", dia_mayor_amplitud)

## EJ 8 
notas = [
    [7, 8, 6], 
    [5, 9, 7], 
    [8, 6, 9],  
    [4, 7, 5],   
    [9, 8, 10]   
]


print("Promedio de cada estudiante:")
for i, fila in enumerate(notas):
    promedio = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {promedio:.2f}")

print("\nPromedio de cada materia:")
num_estudiantes = len(notas)
num_materias = len(notas[0])

for j in range(num_materias):
    suma = 0
    for i in range(num_estudiantes):
        suma += notas[i][j]
    promedio = suma / num_estudiantes
    print(f"Materia {j+1}: {promedio:.2f}")

## EJ 9
tablero = [["-" for _ in range(3)] for _ in range(3)]

jugadores = ["X", "O"]

turno = 0
while turno < 9:
    jugador = jugadores[turno % 2]
    print(f"Turno del jugador {jugador}")
    
    for fila in tablero:
        print(" ".join(fila))
    print() 

    fila_input = int(input("Ingrese fila (0-2): "))
    columna_input = int(input("Ingrese columna (0-2): "))
    
    if tablero[fila_input][columna_input] == "-":
        tablero[fila_input][columna_input] = jugador
        turno += 1
    else:
        print("Casilla ocupada, intente otra vez.\n")

print("Tablero final:")
for fila in tablero:
    print(" ".join(fila))

## EJ 10
ventas = [
    [5, 3, 4, 2, 6, 1, 0], 
    [2, 3, 5, 4, 2, 3, 1], 
    [0, 1, 2, 3, 4, 5, 6],  
    [3, 2, 1, 5, 4, 3, 2]  
]

print("Total vendido por cada producto:")
for i, producto in enumerate(ventas):
    total_producto = sum(producto)
    print(f"Producto {i+1}: {total_producto}")

total_por_dia = []
for dia in range(7):
    suma_dia = sum(ventas[producto][dia] for producto in range(4))
    total_por_dia.append(suma_dia)

mayor_ventas = max(total_por_dia)
dia_mayor_ventas = total_por_dia.index(mayor_ventas) + 1 
print(f"\nDía con mayores ventas totales: Día {dia_mayor_ventas} con {mayor_ventas} ventas")

totales_productos = [sum(producto) for producto in ventas]
max_ventas_producto = max(totales_productos)
producto_mas_vendido = totales_productos.index(max_ventas_producto) + 1
print(f"Producto más vendido de la semana: Producto {producto_mas_vendido} con {max_ventas_producto} unidades")