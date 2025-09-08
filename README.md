# Practicas-de-operadores-aritmeticos.
Practicas de programacion sobre el uso de operadores aritmeticos.
# Sistema de procesamiento de la inforamcion
###################################################################################################################################################################


rograma: Conversión de temperatura °C a K, °F y °R             NOMBRE DEL PROGRAMA

================================================================================================================================
Entrada Input:
Recolección de datos (usuario ingresa °C)
C = float(input("Ingresa la temperatura en °C: "))  # input() pide un string y float() lo convierte a número decimal

============================================================================================================================================
 Procesamiento:
 Transformación de los datos aplicando fórmulas matemáticas
K = C + 273.15     # conversión a Kelvin (273.15 es constante)
F = (9 * C) / 5 + 32   # conversión a Fahrenheit (9/5 y 32 son constantes)
R = F + 459.67     # conversión a Rankine (459.67 es constante)

==========================================================================================================================================================
Almacenamiento:
Los resultados quedan guardados en las variables K, F y R
===========================================================================================================================================================================
Salida (Output):
Mostrar en pantalla los resultados en un formato legible

print(f"{C} °C = {K:.2f} K")   # :.2f limita a 2 decimales
print(f"{C} °C = {F:.2f} °F")
print(f"{C} °C = {R:.2f} °R")
____________________________________________________________________________________________________________________________________________________















===================================================================================================================================================

Programa: Calcular R1 en un divisor de voltaje                         NOMBRE DEL PROGRAMA

=================================================================================================================================================
Entrada (Input):
Usuario ingresa Vi, Vo y R2
Vi = float(input("Ingresa el voltaje de entrada Vi: "))
Vo = float(input("Ingresa el voltaje de salida Vo: "))
R2 = float(input("Ingresa el valor de R2 en ohms: "))

===============================================================================================================================================
Procesamiento:
Despeje de la fórmula del divisor de voltaje para calcular R1
Vo = (R2 / (R1 + R2)) * Vi
R1 = (R2 * Vi / Vo) - R2
R1 = (R2 * Vi / Vo) - R2
=============================================================================================================================================
Almacenamiento:
El resultado queda guardado en la variable R1
==================================================================================================================================================

============================
Salida (Output):
Mostrar el valor de R1 en pantalla
print(f"El valor de R1 es: {R1:.2f} ohms")

===================================================================================================================================================





















==============================================================================================================================================

Programa: Resolver sistema de ecuaciones lineales 2x2 con regla de Cramer        NOMBRE DEL PROGRAMA

===================================================================================================================================================
Entrada (Input):
Usuario ingresa los coeficientes A1, B1, C1, A2, B2, C2

A1= float(input("Ingresa A1: "))
B1= float(input("Ingresa B1: "))
C1= float(input("Ingresa C1: "))
A2= float(input("Ingresa A2: "))
B2= float(input("Ingresa B2: "))
C2= float(input("Ingresa C2: "))

=====================================================================================================================================================
Procesamiento:
Se calcula el determinante y luego x y y con las fórmulas de Cramer
det = A1 * B2 - B1 * A2  # determinante

=================================================================================================================================================
Almacenamiento y Salida (según el caso de la condicional):

if det == 0:    condicionales
    print("El sistema no tiene solución única (determinante = 0)")
else:
    x = (C1 * B2 - B1 * C2) / det
    y = (A1 * C2 - C1 * A2) / det
    # ============================
    # Salida (Output):
    # Mostrar resultados en pantalla
    # ============================
    print(f"Solución: x = {x:.2f}, y = {y:.2f}")  # :.2f limita a 2 decimales


_____________________________________________________________________________________________________________________________________________________




















=====================================================================================================================================================

Programa: Calcular R2 en un regulador de voltaje LM317                                   NOMBRE DEL PROGRAMA

======================================================================================================================================================
Entrada (Input):
Usuario ingresa Vo y R1
Vo = float(input("Ingresa el voltaje de salida Vo: "))
R1 = float(input("Ingresa el valor de R1 en ohms: "))

=====================================================================================================================================================
Procesamiento:
Se aplica la fórmula del LM317
Vo = 1.25 * (1 + R2/R1) + R2 * IADJ
Despejando R2:
R2 = (Vo - 1.25) / ((1.25 / R1) + IADJ)
IADJ = 0.0001  # 100 µA (constante del regulador)
R2 = (Vo - 1.25) / ((1.25 / R1) + IADJ)

===================================================================================================================================================
Almacenamiento:
El valor calculado de R2 queda en la variable R2
===========================================================================================================================================================
Salida (Output):
Mostrar el valor de R2 en pantalla
print(f"El valor de R2 es: {R2:.2f} ohms")

=============================================================================================================================================================
