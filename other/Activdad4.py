'''
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


print("""ALGORITMO #5: VALIDACIÓN Y TIPO DE TRIÁNGULO.

Solicita la longitud de tres segmentos (A, B, C). Primero, determina si pueden 
formar un triángulo (la suma de dos lados siempre debe ser estrictamente 
mayor al tercer lado). Si no es válido, imprime un mensaje. Si es válido, determina 
e imprime si es Equilátero (3 lados iguales), Isósceles (2 lados iguales) o 
Escaleno (3 lados distintos).
""")
try: #intenta
    #pedir las 3 medias de los lados y guardarlas como flotantes
    A = float(input("Ingresa medida del lado A: "))
    B = float(input("Ingresa medida del lado B: "))
    C = float(input("Ingresa medida del lado C: "))
    if (A > 0 and B > 0 and C > 0) and ( A+B >= C or A+C >= B or B+C >= A): #si los tres lados tienen medida mayor a cero
        print("\nLas medias corresponden a un triángulo.")
        if A == B == C:   #A==B and A==C and B==C
            print("Es un triángolo EQUILATERO")
        elif A != B != C:  #A != B and A != C and B != C
            print("Es un triángulo ESCALENO")
        else:
            print("Es un triángulo ISÓSCELES")
    else:
        print("ERROR: Los tres lados deben ser mayores que cero.")
except ValueError: #si encuentras un error haz lo siguiente
    print("ERROR: Ingresa sólo números")
print("20604 Sergio Padilla")

print("""ALGORITMO #8: DEGLOSE DE TIEMPO.

Desglose de Tiempo: Dado un número entero que representa una cantidad 
de tiempo en segundos, conviértelo y desglósalo en Horas, Minutos y Segundos 
exactos (Ejemplo: 4000 segundos = 1 Hora, 6 Minutos, 40 Segundos). 
Imprime el desglose final.
""")
try:
    SEG = int(input("Ingresa la cantidad de tiempo segundos: "))
    if SEG < 0:
        #raise ValueError
        SEG = abs(SEG)
        print("Hey...ingresaste un número negativo pero ya lo corregí por tí   ¬_¬' ")
    HR = SEG//3600   #1 hora = 3600 segundos
    SEG = SEG - HR*3600
    MIN = SEG//60    # 1 min = 60 segundos
    SEG = SEG - MIN*60
    print(f"\nHoras: {HR}, Minutos: {MIN}, Segundos: {SEG}")
except ValueError:
    print("ERROR: Ingresa sólo números enteros positivos.")
'''

print("""Solicitar al usuario tres números. Imprimir los tres números
de mayor a menor.
""")
try:
    n1 = float(input("Ingresa un número: "))
    n2 = float(input("Ingresa otro número: "))
    n3 = float(input("Ingresa otro número: "))
    if n1 >= n2 >= n3:
        print(n1, n2, n3, sep= "     ")
    elif n1 >= n3 >= n2:
        print(n1, n3, n2, sep= "     ")
    elif n2 >= n1 >= n3:
        print(n2, n1, n3, sep= "     ")
    elif n2 >= n3 >= n1:
        print(n2, n3, n1, sep= "     ")
    elif n3 >= n1 >= n2:
        print(n3, n1, n2, sep= "     ")
    elif n3 >= n2 >= n1:
        print(n3, n2, n1, sep= "     ")
    else:
        print("Error. Esta opción nunca debería de haber salido :/")
except ValueError:
    print("ERROR. Ingresa sólo números")
print("\n20604 Sergio Padilla")
