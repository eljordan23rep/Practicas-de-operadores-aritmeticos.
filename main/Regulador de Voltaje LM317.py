print("ingrese los valores para calcular el valor de R2 en un regulador de voltaje LM317")
#(variable)(funcion)(string )
Vo = float(input("Ingresa el voltaje de salida Vo: "))
R1 = float(input("Ingresa el valor de R1 en ohms: "))

IADJ = 0.0001  #   esto es un valor constate 
#operador aritmetico
R2 = (Vo - 1.25) / ((1.25 / R1) + IADJ)
#imprimir en pantalla con el parametro f-string
print(f"El valor de R2 es: {R2:.2f} ohms")
