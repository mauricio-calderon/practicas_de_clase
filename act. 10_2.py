"""Actividad 10

Nombre: Mauricio Calderon
ID: 25966
"""

alumnos = {
    "alumno1": {
        "nombre": "Francisco Villa",
        "edad": 19,
        "correo": "fvilla@mail.com",
        "materias": ['Español','Física','Matematicas']
    },
    "alumno2": {
        "nombre": "Francisco Villa",
        "edad": 19,
        "correo": "fvilla@mail.com",
        "materias": ['Español','Física','Matematicas']
    },
    "alumno3": {
        "nombre": "Francisco Villa",
        "edad": 19,
        "correo": "fvilla@mail.com",
        "materias": ['Español','Física','Matematicas']
    }
}

mascotas = {
    "perro": {
        "raza": "Salchicha",
        "color": "Cafe",
        "caracteristicas": [
            "Largos",
            "Juguetones",
            "Gordo"
        ]
    },
    "gato": {
        "color": "Cafe",
        "caracteristicas": [
            "Suave"
        ]
    }
}

for key, value in alumnos.items():
    print(f"{key.title()}")
    for key, val in value.items():
        if key == "edad":
            print(f"{key.title()}: {val} años")
        elif key == "materias":
            print("Lista de materias:")
            for materia in val:
                print(f"- {materia}")
        else:
            print(f"{key.title()}: {val}")
