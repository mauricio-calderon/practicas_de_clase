"""Calculadora Basica"""

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def suma(numero1, numero2):
    resulado = numero1 + numero2
    return resulado

def resta(numero1, numero2):
    resulado = numero1 - numero2
    return resulado

while True:
    menu()
    opcion = input("Ingrese una opcion: ")
    a = int(input("Ingrese numero1: "))
    b = int(input("Ingrese numero2: "))
    if opcion == "1":
        print(f"{a} + {b} = {suma(a, b)}\n")
    if opcion == "2":
        print(f"{a} - {b} = {resta(a, b)}\n")
    elif opcion == "5":
        print("Saliendo")
        break