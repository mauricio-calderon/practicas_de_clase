"""Examen rápido.

Nombre: Mia Ycied Rubio de la Cruz
ID: 26413
"""
while True:
    gastos = {}
    while True:
        fecha = (input("Ingrese la fecha de su gasto o fin para terminar: "),2).lower()
        print(fecha)
        if fecha == "fin":
            break
        else:
            gasto = float(input("Ingrese el monto del gasto:"))
            if gasto < 0:
                print("Error, el monto no puede ser negativo. Intente de nuevo")
                continue
            else:
                 gastos[fecha] = gasto
    print("RESUMEN DE LA SESIÓN")
    print("Gastos registrados")
    for fecha, gasto in gastos.items():
        print(f"-{fecha}: ${gasto}")
    suma = sum(gastos.values())
    print(f"-Total gastado: ${suma}")
    numero = len(gastos.keys())
    promedio = suma/numero
    print(f"Promedio de gastos: ${promedio}")
    m_alto = max(gastos.values())
    m_bajo = min(gastos.values())
    print(f"Mayor gasto: ${m_alto}")
    print(f"Menor gasto: ${m_bajo}")
    e = input("¿Desea realizar otro analisis? (s/n)")
    if e == "n":
        print("Gracias por utilizar nuestro sistema de registro")
        break
    else:
        continue
input("")
