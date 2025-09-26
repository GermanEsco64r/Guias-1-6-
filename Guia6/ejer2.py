# Ejercicio 2: Verificar aprobación de cursada
def verificar_aprobacion():
    """
    Solicita tres notas y determina si el alumno aprueba la cursada.
    Condiciones: todas > 4 y promedio >= 7
    """
    print("\n--- VERIFICAR APROBACIÓN DE CURSADA ---")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    
    # Verificar que todas las notas sean mayores a 4
    if nota1 > 4 and nota2 > 4 and nota3 > 4:
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 7:
            return f"APROBADO - Promedio: {promedio:.2f}"
        else:
            return f"DESAPROBADO - Promedio insuficiente: {promedio:.2f}"
    else:
        return "DESAPROBADO - Tiene nota(s) inferior(es) a 4"

def prueba_escritorio_aprobacion():
    """Realiza las pruebas de escritorio del ejercicio 2"""
    print("\n" + "="*50)
    print("PRUEBA DE ESCRITORIO - EJERCICIO 2")
    print("="*50)
    
    # Escenario 1: Nota 1: 3, Nota 2: 9, Nota 3: 9
    print("Escenario 1: 3, 9, 9")
    nota1, nota2, nota3 = 3, 9, 9
    if nota1 > 4 and nota2 > 4 and nota3 > 4:
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 7:
            resultado = f"APROBADO - Promedio: {promedio:.2f}"
        else:
            resultado = f"DESAPROBADO - Promedio insuficiente: {promedio:.2f}"
    else:
        resultado = "DESAPROBADO - Tiene nota(s) inferior(es) a 4"
    print(f"Resultado: {resultado}")
    
    # Escenario 2: Nota 1: 6, Nota 2: 8, Nota 3: 10
    print("\nEscenario 2: 6, 8, 10")
    nota1, nota2, nota3 = 6, 8, 10
    if nota1 > 4 and nota2 > 4 and nota3 > 4:
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 7:
            resultado = f"APROBADO - Promedio: {promedio:.2f}"
        else:
            resultado = f"DESAPROBADO - Promedio insuficiente: {promedio:.2f}"
    else:
        resultado = "DESAPROBADO - Tiene nota(s) inferior(es) a 4"
    print(f"Resultado: {resultado}")