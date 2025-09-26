# Ejercicio 5: Cálculo de facturas de internet
print("\nEjercicio 5: Facturas de internet")

for i in range(5):  # 5 clientes
    print(f"\nCliente {i+1}:")
    dni = input("Ingrese DNI del cliente: ")
    
    print("Tipos de servicio:")
    print("1. Internet 30 megas - $750")
    print("2. Internet 50 megas - $1100")
    print("3. Internet 100 megas - $1500 (con 5% de descuento)")
    
    tipo_servicio = int(input("Seleccione el tipo de servicio (1-3): "))
    
    if tipo_servicio == 1:
        monto = 750
        servicio = "Internet 30 megas"
    elif tipo_servicio == 2:
        monto = 1100
        servicio = "Internet 50 megas"
    elif tipo_servicio == 3:
        monto = 1500 * 0.95  # Aplicar 5% de descuento
        servicio = "Internet 100 megas"
    else:
        print("Tipo de servicio inválido")
        continue
    
    print(f"DNI: {dni} | Servicio: {servicio} | Monto a pagar: ${monto:.2f}")