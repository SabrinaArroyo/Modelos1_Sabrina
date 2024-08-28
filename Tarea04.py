
# Calificaciones
calif_1 = 10
calif_2 = 7
calif_3 = 4

# porcentaje de las calificaciones
por_1 = 0.15
por_2 = 0.35
por_3 = 0.50

# Cálculo del promedio ponderado
promedio = calif_1 * por_1 + calif_2 * por_2 + calif_3 * por_3

# resultado
print(f"El promedio ponderado es: {promedio:.2f}")

# Matriz original
matriz = [[1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13]]

# Corrección de la matriz
for fila in matriz: #va a ser una variable temporal que representa cada sublista
    suma = fila[0] + fila[1] + fila[2] #suma los primeros tres y los compara con el cuarto valor
    if fila[3] != suma: # escoges el 3 porque es el 4 valor y ya te diste cuenta de que está mal
        print("Corrigiendo la fila {}: {} debería ser {}".format(fila, fila[3], suma))
        # si if es verdader dice que fila debe ser corregida
        fila[3] = suma
    else:
        print("La fila {} es correcta.".format(fila))

# Mostrar la matriz corregida
print("\nMatriz corregida:")
for fila in matriz:
    print(fila)

