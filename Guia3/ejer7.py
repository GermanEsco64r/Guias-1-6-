# Ejercicio 7: Club deportivo
print("\nEjercicio 7: Estadísticas del club")

# Contadores para cada deporte
contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # tenis, rugby, voley, hockey, futbol
edades_por_deporte = {1: [], 2: [], 3: [], 4: [], 5: []}

deportes = {
    1: "Tenis",
    2: "Rugby", 
    3: "Voley",
    4: "Hockey",
    5: "Fútbol"
}

while True:
    numero_socio = input("Ingrese número de socio (0 para terminar): ")
    if numero_socio == "0":
        break
    
    edad = int(input("Ingrese edad: "))
    print("Tipos de deporte: 1-Tenis, 2-Rugby, 3-Voley, 4-Hockey, 5-Fútbol")
    deporte = int(input("Seleccione deporte (1-5): "))
    
    if deporte in contadores:
        contadores[deporte] += 1
        edades_por_deporte[deporte].append(edad)

# Mostrar resultados
print(f"\nSocios que practican Tenis: {contadores[1]}")
print(f"Socios que practican Fútbol: {contadores[5]}")

print("\nPromedio de edad por deporte:")
for deporte_id, nombre in deportes.items():
    if edades_por_deporte[deporte_id]:
        promedio = sum(edades_por_deporte[deporte_id]) / len(edades_por_deporte[deporte_id])
        print(f"{nombre}: {promedio:.1f} años")