#Calcular Valor de R1 en un divisor de voltaje
#(variable)(tipo de dato)(funcion)(el str se convierte a un int)
Vi = float(input("ingresa el valor de entrada Vi: "))
Vo = float(input("ingresa el valor de salida Vo: "))
R2 = float(input("ingresa el valor de R2 en ohms: "))
R1 = (R2 * Vi / Vo) - R2#operador aritmetico
#impresion en pantalla usando parametro f-string
print(f"el valor de R1 es: {R1: .2f} ohms")

