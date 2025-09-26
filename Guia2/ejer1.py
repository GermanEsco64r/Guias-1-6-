# Ejercicio 1: Cálculo de sueldos para despensa
print("EJERCICIO 1: CÁLCULO DE SUELDOS")
print("=" * 50)

# Solicitar categoría del empleado
print("Categorías disponibles:")
print("1 - Repositor")
print("2 - Cajero") 
print("3 - Supervisor")

categoria = int(input("Ingrese la categoría del empleado (1-3): "))

# Sueldos brutos por categoría
sueldos_brutos = {
    1: 32335,      # Repositor
    2: 38630.89,   # Cajero
    3: 45560.20    # Supervisor
}

categorias_nombres = {
    1: "Repositor",
    2: "Cajero",
    3: "Supervisor"
}

if categoria in [1, 2, 3]:
    sueldo_bruto = sueldos_brutos[categoria]
    
    # Cálculo de descuentos
    descuento_jubilacion = sueldo_bruto * 0.11
    descuento_obra_social = sueldo_bruto * 0.03
    total_descuentos = descuento_jubilacion + descuento_obra_social
    sueldo_neto = sueldo_bruto - total_descuentos
    
    # Mostrar resultados
    print(f"\n--- LIQUIDACIÓN DE SUELDO ---")
    print(f"Categoría: {categorias_nombres[categoria]}")
    print(f"Sueldo Bruto: ${sueldo_bruto:,.2f}")
    print(f"Descuento Jubilación (11%): ${descuento_jubilacion:,.2f}")
    print(f"Descuento Obra Social (3%): ${descuento_obra_social:,.2f}")
    print(f"Total Descuentos: ${total_descuentos:,.2f}")
    print(f"SUELDO NETO: ${sueldo_neto:,.2f}")
    
    # Bono especial para repositores
    if categoria == 1:
        bono_compras = sueldo_bruto * 0.08
        print(f"Bono en compras (8%): ${bono_compras:,.2f}")
else:
    print("Categoría inválida. Debe ser 1, 2 o 3.")