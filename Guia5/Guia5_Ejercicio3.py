notas = []
print("Ingrese las notas de los 40 alumnos (5 notas por alumno):")
for i in range(40):
    print(f"\nAlumno {i+1}:")
    alumno_notas = []
    for j in range(5):
        while True:
            try:
                nota = float(input(f"Nota {j+1}: "))
                if 0 <= nota <= 10:  # Validar que la nota esté entre 0 y 10
                    alumno_notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10")
            except ValueError:
                print("Por favor, ingrese un número válido")
    notas.append(alumno_notas)
#Calcular y mostrar el promedio de cada alumno
print("PROMEDIOS DE LOS ALUMNOS")
print("========================")

for i, alumno in enumerate(notas):
    promedio = sum(alumno) / len(alumno)
    print(f"Alumno {i+1}: Notas: {alumno} → Promedio: {promedio:.2f}")

print("========================")