""" Programa que almacena una lista de nombres"""

nombres = []

while True:
    nom = input("Introduce un nombre: ")
    if nom == "salir":
        break
    nombres.append(nom)

for nombre in nombres:
    print(f" - {nombre}")

i = 0
while i < len(nombres):
    print(nombres[i])
    i += 1