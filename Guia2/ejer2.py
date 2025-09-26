# Ejercicio 2: Mercería - Control de ventas
print("\n" + "="*50)
print("EJERCICIO 2: MERCERÍA - CONTROL DE VENTAS")
print("=" * 50)

# Solicitar cantidad de paquetes
cantidad = int(input("Ingrese la cantidad de paquetes: "))

if cantidad < 5:
    print("❌ No se permiten compras inferiores a 5 productos.")
elif 5 <= cantidad <= 15:
    print(f"✅ Costo de envío: $200")
    print(f"📦 Cantidad de productos: {cantidad}")
else:
    print("✅ ¡ENVÍO GRATUITO!")
    print(f"📦 Cantidad de productos: {cantidad}")