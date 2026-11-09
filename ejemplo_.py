cant = int(input("Cantidad de alumnos: "))

dic_alumnos = {}

for i in range(cant):
    id = input("ID de alumno: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")

    dic_alumnos[id] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }

print(dic_alumnos)