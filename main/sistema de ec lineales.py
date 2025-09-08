A1 = float(input("Ingresa A1: "))
B1 = float(input("Ingresa B1: "))
C1 = float(input("Ingresa C1: "))
A2 = float(input("Ingresa A2: "))
B2 = float(input("Ingresa B2: "))
C2 = float(input("Ingresa C2: "))

det = A1 * B2 - B1 * A2

if det == 0:
    print("El sistema no tiene solución única (determinante = 0)")
else:
    x = (C1 * B2 - B1 * C2) / det
    y = (A1 * C2 - C1 * A2) / det
    print(f"Solución: x = {x:.2f}, y = {y:.2f}")