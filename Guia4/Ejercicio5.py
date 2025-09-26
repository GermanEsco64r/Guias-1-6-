# Ejercicio: Análisis de ventas de vendedores
print("=== ANÁLISIS DE VENTAS ===")

# Vectores con datos de vendedores y ventas
vendedores = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]
ventas = [1500, 3200, 800, 4500, 1200, 2800, 3900, 600, 5100, 1800, 2300, 950, 4200, 1700, 2900]

# Valor del cambio dólar a peso
TIPO_CAMBIO = 140

# Verificar que ambos arreglos tengan la misma longitud
if len(vendedores) != len(ventas):
    print("Error: Los arreglos no tienen la misma cantidad de elementos")
else:
    # Encontrar la mayor venta
    mayor_venta = ventas[0]
    vendedor_mayor = vendedores[0]
    indice_mayor = 0
    
    # Encontrar la menor venta
    menor_venta = ventas[0]
    vendedor_menor = vendedores[0]
    indice_menor = 0
    
    # Recorrer el arreglo para encontrar mayor y menor venta
    for i in range(len(ventas)):
        # Buscar mayor venta
        if ventas[i] > mayor_venta:
            mayor_venta = ventas[i]
            vendedor_mayor = vendedores[i]
            indice_mayor = i
        
        # Buscar menor venta
        if ventas[i] < menor_venta:
            menor_venta = ventas[i]
            vendedor_menor = vendedores[i]
            indice_menor = i
    
    # Calcular conversiones a pesos
    mayor_venta_pesos = mayor_venta * TIPO_CAMBIO
    menor_venta_pesos = menor_venta * TIPO_CAMBIO
    
    # Mostrar resultados
    print(f"\n--- RESULTADOS ---")
    print(f"MAYOR VENTA:")
    print(f"Vendedor: {vendedor_mayor}")
    print(f"Venta en dólares: ${mayor_venta:,.2f}")
    print(f"Venta en pesos: ${mayor_venta_pesos:,.2f}")
    
    print(f"\nMENOR VENTA:")
    print(f"Vendedor: {vendedor_menor}")
    print(f"Venta en dólares: ${menor_venta:,.2f}")
    print(f"Venta en pesos: ${menor_venta_pesos:,.2f}")
    
    # Mostrar todas las ventas para referencia
    print(f"\n--- DETALLE COMPLETO DE VENTAS ---")
    print("Vendedor | Dólares | Pesos")
    print("-" * 30)
    for i in range(len(vendedores)):
        venta_pesos = ventas[i] * TIPO_CAMBIO
        print(f"{vendedores[i]:8} | ${ventas[i]:7,.2f} | ${venta_pesos:9,.2f}")