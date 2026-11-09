print("""ALGORITMO #1: CÁLCULO0 DE RENDIMIENTO DE PRODUCCIÓN.

Cálculo de Rendimiento de Producción: Solicita al usuario el número 
total de piezas fabricadas en un lote y la cantidad de piezas defectuosas. 
Calcula el porcentaje de rendimiento de calidad usando la fórmula
 Rendimiento = [ (Fabricadas - Defectuosas) / (Fabricadas) ]*100. 
 Además, indica el estado del proceso en la salida: "Revisión de máquina 
 requerida" (menor a 90%), "Rendimiento aceptable" (entre 90% y 95%) 
 o "Rendimiento óptimo" (mayor a 95%).
 """)
try:
    fabricado = int(input("Ingresa el total de piezas fabricadas: "))
    defect = int(input("Ingresa la cantidad de piezas defectuosas: "))
    if fabricado >= defect:
        rendimiento = ((fabricado - defect) / fabricado)*100
        print(f"Rendimiento: {round(rendimiento, 1)}%")
        if rendimiento > 95:
            print("Rendimiento óptimo")
        elif rendimiento >= 90 and rendimiento <= 95:
            print("Rendimiento aceptable")
        else:
            print("Revisión de máquina requerida")
    else:
        print("ERROR. Las piezas fabricadas deben ser mayor o igual que las defectuosas.")
except:
    print(">>> ERROR. Ingresa sólo números.")
print("\n20604 Sergio Padilla")
