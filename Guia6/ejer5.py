# Ejercicio 5: Ordenar números
def ordenar_numeros():
    """
    Solicita dos números y los devuelve ordenados de menor a mayor
    """
    print("\n--- ORDENAR NÚMEROS ---")
    a = float(input("Ingrese el primer número (a): "))
    b = float(input("Ingrese el segundo número (b): "))
    
    if a < b:
        return f"Ordenados: {a}, {b}"
    else:
        return f"Ordenados: {b}, {a}"

def prueba_escritorio_ordenar():
    """Realiza las pruebas de escritorio del ejercicio 5"""
    print("\n" + "="*50)
    print("PRUEBA DE ESCRITORIO - EJERCICIO 5")
    print("="*50)
    
    # Escenario 1: a: 5, b: 9
    print("Escenario 1: a=5, b=9")
    a, b = 5, 9
    if a < b:
        resultado = f"Ordenados: {a}, {b}"
    else:
        resultado = f"Ordenados: {b}, {a}"
    print(f"Resultado: {resultado}")
    
    # Escenario 2: a: 8, b: 3
    print("\nEscenario 2: a=8, b=3")
    a, b = 8, 3
    if a < b:
        resultado = f"Ordenados: {a}, {b}"
    else:
        resultado = f"Ordenados: {b}, {a}"
    print(f"Resultado: {resultado}")