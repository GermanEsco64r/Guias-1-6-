# Ejercicio 3: Determinar tipo de triángulo
def tipo_triangulo():
    """
    Solicita los tres lados de un triángulo y determina su tipo:
    - Equilátero: todos los lados iguales
    - Isósceles: dos lados iguales
    - Escaleno: todos los lados diferentes
    """
    print("\n--- DETERMINAR TIPO DE TRIÁNGULO ---")
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    lado3 = float(input("Ingrese el tercer lado: "))
    
    # Verificar que sea un triángulo válido
    if (lado1 + lado2 > lado3 and 
        lado1 + lado3 > lado2 and 
        lado2 + lado3 > lado1):
        
        if lado1 == lado2 == lado3:
            return "Triángulo EQUILÁTERO (todos los lados iguales)"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triángulo ISÓSCELES (dos lados iguales)"
        else:
            return "Triángulo ESCALENO (todos los lados diferentes)"
    else:
        return "❌ ERROR: No es un triángulo válido"

def prueba_escritorio_triangulo():
    """Realiza las pruebas de escritorio del ejercicio 3"""
    print("\n" + "="*50)
    print("PRUEBA DE ESCRITORIO - EJERCICIO 3")
    print("="*50)
    
    # Escenario 1: Lado 1: 10, Lado 2: 15, Lado 3: 20
    print("Escenario 1: 10, 15, 20")
    lado1, lado2, lado3 = 10, 15, 20
    if (lado1 + lado2 > lado3 and 
        lado1 + lado3 > lado2 and 
        lado2 + lado3 > lado1):
        
        if lado1 == lado2 == lado3:
            resultado = "Triángulo EQUILÁTERO (todos los lados iguales)"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            resultado = "Triángulo ISÓSCELES (dos lados iguales)"
        else:
            resultado = "Triángulo ESCALENO (todos los lados diferentes)"
    else:
        resultado = "❌ ERROR: No es un triángulo válido"
    print(f"Resultado: {resultado}")
    
    # Escenario 2: Lado 1: 30, Lado 2: 30, Lado 3: 30
    print("\nEscenario 2: 30, 30, 30")
    lado1, lado2, lado3 = 30, 30, 30
    if (lado1 + lado2 > lado3 and 
        lado1 + lado3 > lado2 and 
        lado2 + lado3 > lado1):
        
        if lado1 == lado2 == lado3:
            resultado = "Triángulo EQUILÁTERO (todos los lados iguales)"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            resultado = "Triángulo ISÓSCELES (dos lados iguales)"
        else:
            resultado = "Triángulo ESCALENO (todos los lados diferentes)"
    else:
        resultado = "❌ ERROR: No es un triángulo válido"
    print(f"Resultado: {resultado}")
    
    # Escenario 3: Lado 1: 20, Lado 2: 20, Lado 3: 30
    print("\nEscenario 3: 20, 20, 30")
    lado1, lado2, lado3 = 20, 20, 30
    if (lado1 + lado2 > lado3 and 
        lado1 + lado3 > lado2 and 
        lado2 + lado3 > lado1):
        
        if lado1 == lado2 == lado3:
            resultado = "Triángulo EQUILÁTERO (todos los lados iguales)"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            resultado = "Triángulo ISÓSCELES (dos lados iguales)"
        else:
            resultado = "Triángulo ESCALENO (todos los lados diferentes)"
    else:
        resultado = "❌ ERROR: No es un triángulo válido"
    print(f"Resultado: {resultado}")