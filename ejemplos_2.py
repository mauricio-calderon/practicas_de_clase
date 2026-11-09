"""Ejemplos con condicionales.

30 de septiembre de 2026"""

print("=== Calculadora Basica ===")
print("Opciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Seleccione una opcion: "))
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if opcion == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif opcion == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif opcion == 3:
    print(f"{num1} x {num2} = {num1 * num2}")
elif opcion == 4:
    if num1 == 0 and num2 == 0:
        print(f"{num1} ÷ {num2} = 1")
    elif num2 == 0:
        print("No se puede dividir por 0")
    else:
        print(f"{num1} ÷ {num2} = {num1 / num2}")
else:
    print("Opcion no valida.")