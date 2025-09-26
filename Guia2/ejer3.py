# Ejercicio 3: Calculadora de compras
print("\n" + "="*50)
print("EJERCICIO 3: CALCULADORA DE COMPRAS")
print("=" * 50)

total_compra = 0

# Ingreso de datos para 3 productos
for i in range(1, 4):
    print(f"\n--- Producto {i} ---")
    precio_kg = float(input(f"Precio por Kg del producto {i}: $"))
    cantidad_kg = float(input(f"Cantidad en Kg del producto {i}: "))
    
    monto_producto = precio_kg * cantidad_kg
    total_compra += monto_producto
    
    print(f"Monto del producto {i}: ${monto_producto:,.2f}")

# Mostrar totales
print(f"\n--- RESUMEN DE COMPRA ---")
print(f"TOTAL DE LA COMPRA: ${total_compra:,.2f}")

# Aplicar descuento si corresponde
if total_compra > 100:
    descuento = total_compra * 0.10
    total_con_descuento = total_compra - descuento
    print(f"🎉 Descuento del 10%: -${descuento:,.2f}")
    print(f"TOTAL CON DESCUENTO: ${total_con_descuento:,.2f}")
else:
    print("ℹ️  No se aplica descuento (compra menor a $100)")