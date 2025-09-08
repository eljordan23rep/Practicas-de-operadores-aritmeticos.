#conversión de °C a K, F y R
#(variable)(tipo de dato)(funcion)(el string se convierte a un float)  
C = float(input("ingresa la temperatura °C: "))
#conversión a Kelvin
K = C + 273.5 #273.5 valor constate
#conversion a Fahrenheit
F = (9 * C) / 5 + 32 #en esta variable estoy usando un operador aritmetico con valores constantes
#conversión a rankine
R = F + 459.67 #459 es constate
#fucion para imprimir el resultado en pantalla
#f "" se usa para poner variables adentro de un texto 
print(f"{C} °C = {K:.2f} K")  #el :. 2f es limite de decimales del tipo de dato float
print(f"{C} °C = {F:.2f} °F")
print(f"{C} °C = {R:.2f} °R")
