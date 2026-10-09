#Cree una aplicacion que lea los datos de un estudiante: nombres, apellidos, nota. Calcular el promedio de las notas, la nota mas alta y la nota mas baja. Mostrar los 3 estudiantes con mayor nota.

estudiantes = []

for i in range(3):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    estudiantes.append((nombre, apellido, nota))

promedio = sum([estudiante[2] for estudiante in estudiantes]) / len(estudiantes)
nota_maxima = max([estudiante[2] for estudiante in estudiantes])
nota_minima = min([estudiante[2] for estudiante in estudiantes])

print(f"Promedio de las notas: {promedio}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[2], reverse=True)
print("Los 3 estudiantes con mayor nota son:")
for i, (nombre, apellido, nota) in enumerate(estudiantes_ordenados[:3]):
    print(f"{i+1}. {nombre} {apellido}: {nota}")