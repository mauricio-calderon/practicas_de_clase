'''
CONTRASEÑA = "sepa20604"
print("EXAMEN PARCIAL 1\n")
contra = input("Ingresa contraseña: ")
if contra == CONTRASEÑA:
    print("*** Contraseña correcta ***")
    try:
        num1 = float(input("Ingresa un numero: "))
        if num1 >= 0:
            print("Número positivo")
        else:
            print("Numero negativo")
        if num1 % 2 == 0:
            print("Número par")
        else:
            print("Número impar")
    except ValueError:
        print("*** Ingresa sólo números ***")
else:
    print("*** Contraseña incorrecta ***")
'''

print("EXAMEN PARCIAL 1\n")
print("""[a] Revisar contraseña
[b] Operaciones""")
opc = input("\nElige una opción: ")
if opc.lower() == "a":
    contraseña = input("Ingresa tu contraseña: ")
    if contraseña == "20604padilla":
        print("*** Acceso correcto.\nSergio Padilla 20604 ***")
    else:
        print("*** Acceso incorrecto ***")
elif opc.lower() == "b":
    try:
        a = float(input("Ingresa un numero 'a': "))
        b = float(input("Ingresa un numero 'b': "))
        r = a*(a+b)**3
        print(f"{a} ({a} + {b})^3 = {r})")
    except ValueError:
        print("*** Ingresa sólo números ***")
else:
    print("*** Opción inválida ***")