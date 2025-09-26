# Ejercicio 6: Carrera automovilística
print("\nEjercicio 6: Mejor tiempo en carrera")

mejor_tiempo = float('inf')  # Inicializar con un valor muy grande
mejor_vehiculo = 0

for i in range(12):  # 12 competidores
    print(f"\nCompetidor {i+1}:")
    vehiculo = int(input("Número de vehículo: "))
    tiempo = float(input("Tiempo en segundos: "))
    
    if tiempo < mejor_tiempo:
        mejor_tiempo = tiempo
        mejor_vehiculo = vehiculo

print(f"\nEl mejor tiempo fue del vehículo {mejor_vehiculo} con {mejor_tiempo} segundos")