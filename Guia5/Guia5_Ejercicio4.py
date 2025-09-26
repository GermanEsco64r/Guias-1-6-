# Definir constantes
NUM_ARTICULOS = 50
NUM_VENDEDORES = 15

# Crear matriz de cantidades (50 artículos x 15 vendedores)
CANT = [[0] * NUM_VENDEDORES for _ in range(NUM_ARTICULOS)]

# Vector para totales por vendedor
TOTAL = [0] * NUM_VENDEDORES

# Función para cargar datos de ventas
def cargar_ventas():
    print("=== CARGA DE VENTAS ===")
    print(f"Ingrese las cantidades vendidas para {NUM_ARTICULOS} artículos y {NUM_VENDEDORES} vendedores")
    print("--------------------------------------------------------")
    
    for i in range(NUM_ARTICULOS):
        print(f"\nArtículo {i+1}:")
        for j in range(NUM_VENDEDORES):
            while True:
                try:
                    cantidad = int(input(f"  Vendedor {j+1}: "))
                    if cantidad >= 0:
                        CANT[i][j] = cantidad
                        break
                    else:
                        print("    La cantidad debe ser mayor o igual a 0")
                except ValueError:
                    print("    Por favor, ingrese un número entero válido")

# Función para cargar datos de ejemplo (para pruebas)
def cargar_datos_ejemplo():
    print("Cargando datos de ejemplo...")
    from random import randint
    for i in range(NUM_ARTICULOS):
        for j in range(NUM_VENDEDORES):
            CANT[i][j] = randint(0, 100)  # Valores aleatorios entre 0 y 100

# Función para calcular totales por vendedor
def calcular_totales():
    for j in range(NUM_VENDEDORES):
        total_vendedor = 0
        for i in range(NUM_ARTICULOS):
            total_vendedor += CANT[i][j]
        TOTAL[j] = total_vendedor

# Función para encontrar el vendedor con mayor venta
def encontrar_mejor_vendedor():
    max_venta = 0
    mejor_vendedor = 0
    
    for j in range(NUM_VENDEDORES):
        if TOTAL[j] > max_venta:
            max_venta = TOTAL[j]
            mejor_vendedor = j + 1  # +1 porque los vendedores se numeran del 1 al 15
    
    return mejor_vendedor, max_venta

# Función para mostrar resumen de ventas
def mostrar_resumen():
    print("\n" + "="*60)
    print("RESUMEN DE VENTAS")
    print("="*60)
    
    # Mostrar totales por vendedor
    print("\nTOTAL DE VENTAS POR VENDEDOR:")
    print("-" * 30)
    for j in range(NUM_VENDEDORES):
        print(f"Vendedor {j+1}: {TOTAL[j]} unidades")
    
    # Encontrar y mostrar el mejor vendedor
    mejor_v, total_mejor = encontrar_mejor_vendedor()
    print("\n" + "="*60)
    print(f"🏆 MEJOR VENDEDOR: Vendedor {mejor_v}")
    print(f"   Total vendido: {total_mejor} unidades")
    print("="*60)

# Función principal
def main():
    print("SISTEMA DE GESTIÓN DE VENTAS")
    print("=============================")
    
    # Preguntar si usar datos de ejemplo o cargar manualmente
    while True:
        opcion = input("\n¿Desea cargar datos manualmente (M) o usar datos de ejemplo (E)? ").upper()
        if opcion == 'M':
            cargar_ventas()
            break
        elif opcion == 'E':
            cargar_datos_ejemplo()
            break
        else:
            print("Opción no válida. Por favor ingrese M o E.")
    
    # Calcular totales
    calcular_totales()
    
    # Mostrar resultados
    mostrar_resumen()

# Ejecutar el programa
if __name__ == "__main__":
    main()