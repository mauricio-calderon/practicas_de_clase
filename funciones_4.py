"""Sistema de registro de usuarios"""
import archivo_auxiliar
# ==== Flujo principal ====
lista_diccionario = []
while True:
    archivo_auxiliar.imprimir_menu()
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        archivo_auxiliar.crear_registro(lista_diccionario)
    elif opcion == 2:
        archivo_auxiliar.imprimir_datos(lista_diccionario)
    elif opcion == 3:
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida")




