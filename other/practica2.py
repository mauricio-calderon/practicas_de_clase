un_titulo = "Masa de aire frío llegará a México; ¿qué estados tendrán descenso de temperaturas?"
un_parrafo = "El Servicio Meteorológico Nacional (SMN) informó que entre el martes 15 y el jueves 17 de septiembre de 2026, una masa de aire frío se desplazará sobre el golfo de México, lo que ocasionará descenso de las temperaturas en estados de las regiones norte, oriente y centro del país."
un_numero = "123456789.05"
otra_cosa = "a1b2c3"

#print(un_titulo)
#print(un_titul.capitalize())
#print(un_titulo.casefold())
#print(un_titulo.lower())
#print(len(un_titulo))
#print(un_titulo.center(100).upper())
#print(un_titulo[ 0:15:5])
#print(un_parrafo)
#print(un_parrafo.upper().count("S", 4, 15))
#print(un_parrafo[26:34])
#print(un_parrafo[26:34].lower().endswith("al"))
#print(un_parrafo[26:34].lower().startswith("na"))
#print(un_parrafo.lower().count("de"))
#pos = un_parrafo.lower().find("de")
#print(un_titulo.title())
#print(un_numero,un_numero.isalpha()) #sólo letras
#print(otra_cosa,otra_cosa.isalpha())
#print(un_numero,un_numero.isalnum()) #solo letras y números
#print(otra_cosa,otra_cosa.isalnum())
#print(un_numero,un_numero.isdigit()) #solo números
#print("-55","-55".isdigit())
#print("-10","-10".isdecimal())
#print(un_numero,un_numero.isnumeric())
'''
if un_numero.isdigit() == True:
    print(un_numero, "Sólo hay números")
else:
    print(un_numero,"Nó es un número")

try:
    if float("sdffgsrdd"):
        print(un_numero, "Sólo hay números")
except ValueError:
    print("Tipo de dato inválido")
'''
email = input("Ingresa tu email: ")
if "@" in email:
    print("Correo válido")
elif "#" in email:
    print("Correo invalido")
else:
    print("Correo invalido")