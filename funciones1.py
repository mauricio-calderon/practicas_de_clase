# Funciones comunes de Python
"""print("Hola Mundo!")
lista = [1, 2, 3, 4, 5, 6]
print(len(lista))"""

# nombre_funcion(argumento)

#CREACION DE FUNCIONES
"""def saludos():
    print("Hola Mundo! 1")
    print("Hola Mundo! 2")
    print("Hola Mundo! 3")
    print("Hola Mundo! 4")

# LLAMADA DE FUNCION
saludos()
saludos()
saludos()"""


def promedio(lista):
    suma = sum(lista)
    t_elem = len(lista)
    promedio = suma / t_elem
    return promedio

lista = [1, 2, 3, 4, 5, 6]
prom = promedio(lista)
print(prom)

print(promedio(lista))





