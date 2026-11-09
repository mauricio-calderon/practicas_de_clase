print("\nEXAMEN RÁPIDO #1: CALCULADORA\n")
#print("[1] Sumar\n[2] Restar\n[3] Multiplicar\n[4] Dividir\n")
print("""[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
""")
opc = int(input("Elige una opción: "))

if opc == 1:
    print("\nSUMA")
    num1 = float(input("Ingresa un numero: "))
    num2 = float(input("Ingresa otro numero: "))
    r = num1 + num2
    print(f"{num1} + {num2} = {r}")
elif opc == 2:
    print("\nRESTAR")
    num1 = float(input("Ingresa un numero: "))
    num2 = float(input("Ingresa otro numero: "))
    r = num1 - num2
    print(f"{num1} - {num2} = {r}")
elif opc == 3:
    print("\nMULTIPLICAR")
    num1 = float(input("Ingresa un numero: "))
    num2 = float(input("Ingresa otro numero: "))
    r = num1 * num2
    print(f"{num1} x {num2} = {r}")
elif opc == 4:
    print("\nDIVIDIR")
    num1 = float(input("Ingresa un numero: "))
    num2 = float(input("Ingresa otro numero: "))
    r = num1 / num2
    print(f"{num1} / {num2} = {r}")
else:
    print("ERROR. OPCIÓN INVÁLIDA")

print("Bye!")