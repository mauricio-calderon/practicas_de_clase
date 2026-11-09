"""Actividad 9. Sistema de registro de materias

Nombre: Mauricio Calderon
ID: 25966
"""
print(
    "=========================\n"
    "  Materias disponibles\n"
    "=========================\n"
    "1. Español\n"
    "2. Matemáticas\n"
    "3. Física\n"
    "4. Química\n"
    "5. Biología\n"
    "6. Inglés\n"
    "=========================\n"
)

no_mat = int(input(
    "¿Cuantas materias va a registrar?"
    "(Max. 6, Min. 2): ")
)

if no_mat > 6 or no_mat < 2:
    print("No. de materias fuera del rango. Se registraran 3.")
    no_mat = 3
else:
    print(f"Se registraran {no_mat} materias.")

materias = [
    "Español",
    "Matemáticas",
    "Física",
    "Química",
    "Biología",
    "Inglés"
]
mat_reg = []
for i in range(no_mat):
    mat = input(f"Ingrese materia {i+1}: ")
    if mat not in materias:
        print("Materia no valida. Se omitira registro.")
    elif mat not in mat_reg and mat in materias:
        mat_reg.append(mat)
        print(
            f"Materia {mat} "
            f"registrada correctamente."
        )
    elif mat in mat_reg:
        print(
            f"La materia {mat} ya se registro."
            f" Se omitira registro."
        )

print(
    "=========================\n"
    "    Materias incritas\n"
    "=========================\n"
)
for i, mat in enumerate(mat_reg, start=1):
    print(f"Materia {i}: {mat}")