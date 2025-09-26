# Ejercicio 8: Procesamiento de censo
print("\nEjercicio 8: Censo provincial")

total_personas = 0
varones = 0
mujeres = 0
varones_16_60 = 0

while True:
    documento = input("Ingrese número de documento (0 para terminar): ")
    
    if documento == "0":
        break
    
    edad = int(input("Ingrese edad: "))
    sexo = input("Ingrese sexo (F/M): ").upper()
    
    total_personas += 1
    
    if sexo == 'M':
        varones += 1
        if 16 <= edad <= 60:
            varones_16_60 += 1
    elif sexo == 'F':
        mujeres += 1

# Calcular porcentajes
if varones > 0:
    porcentaje_varones_16_60 = (varones_16_60 / varones) * 100
else:
    porcentaje_varones_16_60 = 0

# Mostrar resultados
print(f"\n--- RESULTADOS DEL CENSO ---")
print(f"Total de personas censadas: {total_personas}")
print(f"Cantidad de varones: {varones}")
print(f"Cantidad de mujeres: {mujeres}")
print(f"Porcentaje de varones entre 16 y 60 años: {porcentaje_varones_16_60:.1f}%")