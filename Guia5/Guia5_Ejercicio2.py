# Crear una matriz de 4x4
matriz = []

# Rellenar la matriz
for i in range(4):
    fila = []
    for j in range(4):
        # Poner 1 en la diagonal (donde i == j), 0 en el resto
        if i + j == 3:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

# Mostrar la matriz por pantalla
print("Matriz 4x4 con unos en la diagonal:")
print("-----------------------------------")
for fila in matriz:
    # Convertir cada elemento a string y unirlos con tabulaciones
    print("\t".join(str(elemento) for elemento in fila))
print("-----------------------------------")