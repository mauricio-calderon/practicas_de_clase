"""Actividad 7. Registro de nombres

Nombre: Mauricio Calderon
ID: 25966
"""
# esto es un comentario

# Pide el numero de nombres
cant = int(input("Introduce la cantidad nombres: "))
nombres = []

# Pedir la lista de nombres y guardarla en una variable
for i in range(cant):
    nombres.append(input(f"Introduce el nombre {i+1}: "))

# Estas listas guardan los nombres clasificados
cortos = []
medianos = []
largos = []

# Realiza el analisis de los nombres
if nombres:
    for nom in nombres:
        if len(nom) < 5:
            print(f"El nombre {nom} es un nombre CORTO")
            cortos.append(nom)
        elif len(nom) >= 5 and len(nom) <= 7:
            print(f"El nombre {nom} es un nombre MEDIANO")
            medianos.append(nom)
        else:
            print(f"El nombre {nom} es un nombre LARGO")
            largos.append(nom)

    # Impresion de Resultados
    mas_largo = max(nombres, key=len)
    mas_corto = min(nombres, key=len)
    print(f"Hay {len(cortos)} nombres cortos.")
    print(f"Hay {len(medianos)} nombres medianos.")
    print(f"Hay {len(largos)} nombres largos.")
    print(f"El nombre mas largo es {mas_largo} con {len(mas_largo)} letras.")
    print(f"El nombre mas corto es {mas_corto} con {len(mas_corto)} letras.")
else:
    print(f"La lista de nombres esta vacia.")
