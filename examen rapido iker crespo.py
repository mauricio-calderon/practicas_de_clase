while True:
    gastos={}
    print("---REGISTRO DE GASTOS---")
    while True:
        fecha=input("ingresa la fecha del gasto(o 'fin' para termiar):")
        if fecha=="fin":
            break
        monto=float(input("ingresa la monto del gasto:"))

        while monto<0:
            print("ERROR:el monto no puede ser negativo")
            monto=float(input("ingresa el monto del gasto:"))

        if len(gastos)==0:
            print("no se registraron gastos")
        else:
            print("---LISTA DE GASTOS---")

        montos=[]

        for monto in gastos:
            montos.append(monto)

        iker=0

        for monto in montos:
            total=iker+monto
            promedio=total/len(gastos)
            mayor=max(gastos)
            menor=min(gastos)


            if promedio>1:
                print("---PROGRAMA DE GASTOS---")
                print(f"total de gastos:{total}")
                print(f"promedio de gastos:{promedio}")
                print(f"mayor de gastos:{mayor}")
                print(f"menor de gastos:{menor}")
                print("gracias por utilizar el sistema de registro, ¡hasta pronto!")

           











