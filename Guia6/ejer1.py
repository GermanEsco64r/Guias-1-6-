# Ejercicio 1: Comparar edades de hermanos
def comparar_edades():
    """
    Solicita las edades de dos hermanos y determina cuál es mayor
    y la diferencia de edad.
    """
    print("--- COMPARAR EDADES DE HERMANOS ---")
    edad1 = int(input("Ingrese la edad del primer hermano: "))
    edad2 = int(input("Ingrese la edad del segundo hermano: "))
    
    if edad1 > edad2:
        diferencia = edad1 - edad2
        return f"El primer hermano es mayor. Diferencia: {diferencia} años"
    elif edad2 > edad1:
        diferencia = edad2 - edad1
        return f"El segundo hermano es mayor. Diferencia: {diferencia} años"
    else:
        return "Ambos hermanos tienen la misma edad"

# Prueba de escritorio
def prueba_escritorio_edades():
    """Realiza las pruebas de escritorio del ejercicio 1"""
    print("\n" + "="*50)
    print("PRUEBA DE ESCRITORIO - EJERCICIO 1")
    print("="*50)
    
    # Escenario 1: Hermano 1: 25, Hermano 2: 29
    print("Escenario 1: 25 y 29 años")
    edad1, edad2 = 25, 29
    if edad1 > edad2:
        diferencia = edad1 - edad2
        resultado = f"El primer hermano es mayor. Diferencia: {diferencia} años"
    elif edad2 > edad1:
        diferencia = edad2 - edad1
        resultado = f"El segundo hermano es mayor. Diferencia: {diferencia} años"
    else:
        resultado = "Ambos hermanos tienen la misma edad"
    print(f"Resultado: {resultado}")
    
    # Escenario 2: Hermano 1: 23, Hermano 2: 18
    print("\nEscenario 2: 23 y 18 años")
    edad1, edad2 = 23, 18
    if edad1 > edad2:
        diferencia = edad1 - edad2
        resultado = f"El primer hermano es mayor. Diferencia: {diferencia} años"
    elif edad2 > edad1:
        diferencia = edad2 - edad1
        resultado = f"El segundo hermano es mayor. Diferencia: {diferencia} años"
    else:
        resultado = "Ambos hermanos tienen la misma edad"
    print(f"Resultado: {resultado}")
    
    # Escenario 3: Hermano 1: 20, Hermano 2: 20
    print("\nEscenario 3: 20 y 20 años")
    edad1, edad2 = 20, 20
    if edad1 > edad2:
        diferencia = edad1 - edad2
        resultado = f"El primer hermano es mayor. Diferencia: {diferencia} años"
    elif edad2 > edad1:
        diferencia = edad2 - edad1
        resultado = f"El segundo hermano es mayor. Diferencia: {diferencia} años"
    else:
        resultado = "Ambos hermanos tienen la misma edad"
    print(f"Resultado: {resultado}")