def main():
    # Solicitar la cantidad de notas a cargar
    while True:
        try:
            n = int(input("¿Cuántas notas desea cargar? "))
            if n > 0:
                break
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    # Crear el vector para almacenar las notas
    notas = []
    
    # Cargar las notas
    print(f"\nIngrese las {n} notas (valores entre 0 y 10):")
    print("----------------------------------------")
    
    for i in range(n):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("  Error: La nota debe estar entre 0 y 10")
            except ValueError:
                print("  Error: Ingrese un número válido")
    
    # Contar aprobados y desaprobados
    aprobados = 0
    desaprobados = 0
    
    for nota in notas:
        if nota >= 6:
            aprobados += 1
        else:
            desaprobados += 1
    
    # Calcular porcentajes
    porcentaje_aprobados = (aprobados / n) * 100 if n > 0 else 0
    porcentaje_desaprobados = (desaprobados / n) * 100 if n > 0 else 0
    
    # Mostrar resultados
    print("\n" + "="*50)
    print("RESULTADOS")
    print("="*50)
    print(f"Notas cargadas: {notas}")
    print(f"Cantidad total de notas: {n}")
    print(f"Aprobados (≥ 6): {aprobados} ({porcentaje_aprobados:.1f}%)")
    print(f"Desaprobados (< 6): {desaprobados} ({porcentaje_desaprobados:.1f}%)")
    
    # Mostrar estadísticas adicionales
    if n > 0:
        print(f"Nota más alta: {max(notas)}")
        print(f"Nota más baja: {min(notas)}")
        print(f"Promedio general: {sum(notas)/n:.2f}")
    print("="*50)

# Ejecutar el programa
if __name__ == "__main__":
    main()