def main():
    # Solicitar la cantidad de productos
    n = int(input("¿Cuántos productos deseas registrar? "))
    
    # Inicializar listas vacías
    cantidades = []
    costos = []
    nombres_productos = []
    
    # Ingresar datos de cada producto
    print("\nIngresa los datos de cada producto:")
    for i in range(n):
        print(f"\n--- Producto {i + 1} ---")
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        costo = float(input("Costo unitario: $"))
        
        nombres_productos.append(nombre)
        cantidades.append(cantidad)
        costos.append(costo)
    
    # Calcular el precio total y productos que superan $1000
    precio_total = 0
    productos_superan_1000 = []
    
    for i in range(len(cantidades)):
        costo_producto_actual = cantidades[i] * costos[i]
        precio_total += costo_producto_actual

        if costo_producto_actual > 1000:
            productos_superan_1000.append({
                "nombre": nombres_productos[i],
                "costo_total": costo_producto_actual
            })
    
    # Mostrar resultados
    print("\n" + "-------------------------------------------")
    print(f"El precio total de la compra es: ${precio_total:.2f}")
    print("-------------------------------------------")
    print("Productos cuyo costo total supera los $1000:")
    print("-------------------------------------------")

    if len(productos_superan_1000) > 0:
        for producto in productos_superan_1000:
            print(f"- {producto['nombre']}: ${producto['costo_total']:.2f}")
    else:
        print("Ningún producto superó los $1000 de costo total.")
    
    print("-------------------------------------------")
    
    # Mostrar resumen completo 
    print("\nRESUMEN COMPLETO:")
    print("----------------")
    for i in range(len(cantidades)):
        costo_total = cantidades[i] * costos[i]
        print(f"{nombres_productos[i]}: {cantidades[i]} x ${costos[i]:.2f} = ${costo_total:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()