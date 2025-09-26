# Producto 1
precio1 = float(input("Ingrese el precio por Kg del producto 1: "))
kg1 = float(input("Ingrese la cantidad en Kg del producto 1: "))

# Producto 2
precio2 = float(input("Ingrese el precio por Kg del producto 2: "))
kg2 = float(input("Ingrese la cantidad en Kg del producto 2: "))

# Producto 3
precio3 = float(input("Ingrese el precio por Kg del producto 3: "))
kg3 = float(input("Ingrese la cantidad en Kg del producto 3: "))

# Cálculo de montos por producto
total1 = precio1 * kg1
total2 = precio2 * kg2
total3 = precio3 * kg3

print(f"Monto del producto 1: ${total1:.2f}")
print(f"Monto del producto 2: ${total2:.2f}")
print(f"Monto del producto 3: ${total3:.2f}")

# Total de la compra
total_compra = total1 + total2 + total3
print(f"Total de la compra: ${total_compra:.2f}")

# Aplicar descuento si corresponde
if total_compra > 100:
    descuento = total_compra * 0.10
    nuevo_total = total_compra - descuento
    print(f"Se aplica un descuento del 10% (${descuento:.2f}).")
    print(f"Nuevo total a pagar: ${nuevo_total:.2f}")
