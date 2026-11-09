"""Actividad 10

Nombre: Mauricio Calderon
ID: 25966
"""

alumno1 = {
    "nombre": "Francisco Villa",
    "edad": 19,
    "correo": "fvilla@mail.com",
    "materias": ['Español','Física','Matematicas']
}

for key, value in alumno1.items():
    if key == "edad":
        print(f"{key.title()}: {value} años")
    elif key == "materias":
        print("Lista de materias:")
        for materia in value:
            print(f"- {materia}")
    else:
        print(f"{key.title()}: {value}")