# Ejercicio 4: Sistema de sueldos para empresa
print("\n" + "="*50)
print("EJERCICIO 4: SISTEMA DE SUELDOS")
print("=" * 50)

# Ingreso de datos del empleado
dni = input("Ingrese el DNI del empleado: ")
print("\nCategorías disponibles:")
print("0 - Maestranza")
print("1 - Administración")
print("2 - Gerencia")

categoria = int(input("Ingrese la categoría (0-2): "))

# Definición de categorías
categorias = {
    0: {
        'nombre': 'Maestranza',
        'sueldo_bruto': 23600,
        'jubilacion': 0.11,
        'obra_social': 0.03,
        'club': 0.00
    },
    1: {
        'nombre': 'Administración',
        'sueldo_bruto': 35800,
        'jubilacion': 0.11,
        'obra_social': 0.05,
        'club': 0.00
    },
    2: {
        'nombre': 'Gerencia',
        'sueldo_bruto': 60420,
        'jubilacion': 0.11,
        'obra_social': 0.05,
        'club': 0.04
    }
}

if categoria in [0, 1, 2]:
    datos_categoria = categorias[categoria]
    
    # Cálculo de descuentos
    sueldo_bruto = datos_categoria['sueldo_bruto']
    desc_jubilacion = sueldo_bruto * datos_categoria['jubilacion']
    desc_obra_social = sueldo_bruto * datos_categoria['obra_social']
    desc_club = sueldo_bruto * datos_categoria['club']
    
    total_descuentos = desc_jubilacion + desc_obra_social + desc_club
    sueldo_neto = sueldo_bruto - total_descuentos
    
    # Mostrar liquidación
    print(f"\n--- LIQUIDACIÓN DE SUELDO ---")
    print(f"DNI: {dni}")
    print(f"Categoría: {datos_categoria['nombre']}")
    print(f"Sueldo Bruto: ${sueldo_bruto:,.2f}")
    print(f"Descuento Jubilación ({datos_categoria['jubilacion']*100}%): ${desc_jubilacion:,.2f}")
    print(f"Descuento Obra Social ({datos_categoria['obra_social']*100}%): ${desc_obra_social:,.2f}")
    
    if categoria == 2:
        print(f"Descuento Club ({datos_categoria['club']*100}%): ${desc_club:,.2f}")
    
    print(f"Total Descuentos: ${total_descuentos:,.2f}")
    print(f"SUELDO NETO: ${sueldo_neto:,.2f}")
    
else:
    print("❌ Categoría inválida. Debe ser 0, 1 o 2.")