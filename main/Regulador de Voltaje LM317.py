#regulador de voltaje
#(variable)(funcion)(string se convierte a un int)
Vo = float(input("Ingresa el voltaje de salida Vo: "))
R1 = float(input("Ingresa el valor de R1 en ohms: "))

IADJ = 0.0001  # 100 µA  esto es una variable constate 
#operador aritmetico
R2 = (Vo - 1.25) / ((1.25 / R1) + IADJ)
#imprimir en pantalla con el parametro f-string
print(f"El valor de R2 es: {R2:.2f} ohms")