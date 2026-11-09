# ==== Funciones Auxiliares ====
def crear_diccionario(
        prim_nombre,
        prim_apellido,
        seg_apellido,
        edad,
        carrera,
        seg_nombre=""):
    """Crea el diccionario con los datos del alumno"""
    diccionario = {
        "primer_nombre": prim_nombre,
        "segundo_nombre": seg_nombre,
        "primer_apellido": prim_apellido,
        "segundo_apellido": seg_apellido,
        "edad": edad,
        "carrera": carrera,
    }
    return diccionario

def formatear_nombre(usuario):
    f_nombre = f"{usuario["primer_nombre"]} {usuario["segundo_nombre"]} {usuario["primer_apellido"]} {usuario["segundo_apellido"]}"
    return f_nombre.title()

def pedir_datos():
    p_nom = input("Primer nombre: ")
    s_nom = input("Segundo nombre: ")
    p_app = input("Primer apellido: ")
    s_app = input("Segundo apellido: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    return p_nom, s_nom, p_app, s_app, edad, carrera

def imprimir_menu():
    print("Opciones:")
    print("  1. Crear diccionario")
    print("  2. Imprimir todos los datos")
    print("  3. Salir")

def crear_registro(lista_diccionario):
    # p_nom, s_nom, p_app, s_app, edad, carrera
    nom_1, nom_2, ap_1, ap_2, ed, carr = pedir_datos()
    diccionario = crear_diccionario(nom_1, ap_1, ap_2, ed, carr, nom_2)
    lista_diccionario.append(diccionario)
    nombre = formatear_nombre(diccionario)
    print(f"El usuario {nombre} ha sido registrado.")

def imprimir_datos(lista):
    """Función que imprime los datos del registro"""
    for diccionario in lista:
        print(diccionario)