# Ejercicio 4: Verificar año bisiesto
def es_bisiesto():
    """
    Determina si un año es bisiesto según las reglas:
    - Divisible por 4
    - Excepto si es divisible por 100 pero no por 400
    """
    print("\n--- VERIFICAR AÑO BISIESTO ---")
    año = int(input("Ingrese el año: "))
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return f"✅ {año} es un año BISIESTO"
    else:
        return f"❌ {año} NO es un año bisiesto"

def prueba_escritorio_bisiesto():
    """Realiza las pruebas de escritorio del ejercicio 4"""
    print("\n" + "="*50)
    print("PRUEBA DE ESCRITORIO - EJERCICIO 4")
    print("="*50)
    
    # Escenario 1: Años bisiestos
    años_bisiestos = [1996, 2004, 2000, 1600]
    print("Escenario 1: Años BISIESTOS")
    for año in años_bisiestos:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            resultado = f"✅ {año} es un año BISIESTO"
        else:
            resultado = f"❌ {año} NO es un año bisiesto"
        print(f"{año}: {resultado}")
    
    # Escenario 2: Años NO bisiestos
    años_no_bisiestos = [1700, 1800, 1900, 2100]
    print("\nEscenario 2: Años NO BISIESTOS")
    for año in años_no_bisiestos:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            resultado = f"✅ {año} es un año BISIESTO"
        else:
            resultado = f"❌ {año} NO es un año bisiesto"
        print(f"{año}: {resultado}")