print("Solucion a la ecuacion de primer grado con el metodo de Cramer")
#variable(tipodedato)(funcion)(string)
A1 = float(input("Ingresa A1: "))
B1 = float(input("Ingresa B1: "))
C1 = float(input("Ingresa C1: "))
A2 = float(input("Ingresa A2: "))
B2 = float(input("Ingresa B2: "))
C2 = float(input("Ingresa C2: "))

determinante = A1 * B2 - B1 * A2
#condicionales: si el determinante es igual a 0 se imprime la condicion if 
if determinante == 0:
    print("no se puede resolver porque el determinante es = 0")
else:
    x = (C1 * B2 - B1 * C2) / determinante
    y = (A1 * C2 - C1 * A2) / determinante
    print(f"Solución: x = {x:.2f}, y = {y:.2f}")
