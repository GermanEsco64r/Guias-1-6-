# Crear una matriz de 4x4 para las notas y promedios
# Las primeras 3 columnas son para las notas, la 4ta para el promedio
tabla_notas = [[0.0] * 4 for _ in range(4)]

def cargar_notas():
    """Función para cargar las notas de los 4 alumnos"""
    print("=== CARGA DE NOTAS ===")
    print("Ingrese las 3 notas para cada alumno (valores entre 0 y 10)")
    print("----------------------------------------------------------")
    
    for i in range(4):  # 4 alumnos
        print(f"\nAlumno {i+1}:")
        for j in range(3):  # 3 notas por alumno
            while True:
                try:
                    nota = float(input(f"  Nota {j+1}: "))
                    if 0 <= nota <= 10:
                        tabla_notas[i][j] = nota
                        break
                    else:
                        print("    Error: La nota debe estar entre 0 y 10")
                except ValueError:
                    print("    Error: Ingrese un número válido")

def calcular_promedios():
    """Función para calcular los promedios de cada alumno"""
    for i in range(4):
        suma_notas = sum(tabla_notas[i][:3])  # Sumar las 3 primeras notas
        promedio = suma_notas / 3
        tabla_notas[i][3] = round(promedio, 2)  # Guardar el promedio en la 4ta columna

def mostrar_resultados():
    """Función para mostrar las notas y promedios de forma organizada"""
    print("\n" + "="*50)
    print("REPORTE DE NOTAS Y PROMEDIOS")
    print("="*50)
    print("Alumno\tNota 1\tNota 2\tNota 3\tPromedio")
    print("-"*50)
    
    for i in range(4):
        print(f"{i+1}", end="\t")
        for j in range(4):
            print(f"{tabla_notas[i][j]}", end="\t")
        print()  # Nueva línea después de cada alumno
    
    print("="*50)

def main():
    """Función principal del programa"""
    print("SISTEMA DE GESTIÓN DE NOTAS")
    print("============================")
    
    # Cargar las notas
    cargar_notas()
    
    # Calcular los promedios
    calcular_promedios()
    
    # Mostrar los resultados
    mostrar_resultados()

# Ejecutar el programa
if __name__ == "__main__":
    main()