def main():
    # Solicitar la cantidad de productos
    n = int(input("Ingrese la cantidad de productos: "))
    
    # Crear los vectores para cantidades y costos
    cantidades = []
    costos = []
    
    # Llenar los vectores con los datos
    print("\nIngrese los datos de cada producto:")
    for i in range(n):
        print(f"\nProducto {i + 1}:")
        cantidad = int(input("Cantidad: "))
        costo = float(input("Costo unitario: $"))
        
        cantidades.append(cantidad)
        costos.append(costo)
    
    # Calcular el precio total
    precio_total = 0
    for i in range(n):
        precio_total += cantidades[i] * costos[i]
    
    # Encontrar productos que superan los $1000
    productos_superiores = []
    for i in range(n):
        precio_producto = cantidades[i] * costos[i]
        if precio_producto > 1000:
            productos_superiores.append((i + 1, cantidades[i], costos[i], precio_producto))
    
    # Mostrar resultados
    print("\n" + "="*50)
    print("INFORME DE PRODUCTOS")
    print("="*50)
    print(f"Precio total de todos los productos: ${precio_total:.2f}")
    print("\nProductos que superan los $1000:")
    print("-" * 40)
    
    if productos_superiores:
        for producto in productos_superiores:
            print(f"Producto {producto[0]}:")
            print(f"  Cantidad: {producto[1]}")
            print(f"  Costo unitario: ${producto[2]:.2f}")
            print(f"  Precio total: ${producto[3]:.2f}")
            print("-" * 20)
    else:
        print("No hay productos que superen los $1000")
    
    # Mostrar todos los productos (opcional)
    print("\nResumen de todos los productos:")
    print("-" * 30)
    for i in range(n):
        precio = cantidades[i] * costos[i]
        print(f"Producto {i + 1}: {cantidades[i]} unidades x ${costos[i]:.2f} = ${precio:.2f}")

if __name__ == "__main__":
    main()