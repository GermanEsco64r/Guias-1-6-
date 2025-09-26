# Crear una matriz de 4x4 llena de ceros
matriz = [[0 for _ in range(4)] for _ in range(4)]

# Mostrar la matriz por pantalla
print("Matriz 4x4 rellena con ceros:")
print("-----------------------------")
for fila in matriz:
    # Convertir cada elemento a string y unirlos con tabulaciones
    print("\t".join(str(elemento) for elemento in fila))
print("-----------------------------")