while True:
    datos = {}
    while True:
         fecha = input("Ingrese la fecha (o fin): ")
         if fecha == "fin":
             break
         monto = float(input("Ingrese el monto: "))
         while monto < 0:
             monto = float(input("Ingrese el monto otra vez: "))
         datos[fecha] = monto

    print()
    print("--- RESUMEN DE LA SESIÓN ---")
    print("Gastos registrados:")

    for f, m in datos.items():
        print(f"* Fecha {f} -> ${m}")

    gastos = datos.values()
    total = sum(gastos)
    promedio = total / len(gastos)
    maximo = max(gastos)
    minimo = min(gastos)

    print(f"Total: ${total}")
    print(f"Promedio: ${promedio}")
    print(f"Maximo: ${maximo}")
    print(f"Minimo: ${minimo}")

    repuesta = input("¿Desea continuar? [S/N] ")
    if repuesta == "N":
        print("--- Adios ---")
        break