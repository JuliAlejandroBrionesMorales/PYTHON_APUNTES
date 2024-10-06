"""
EJERCICIO 4

Pedir 2 numeros al usuario y hacer todas las operaciones básicas de una calculadora y 
mostrarlo por pantalla

"""

usuario_1 = int(input("Dime el número 1 para hacer las operaciones "))
usuario_2 = int(input("Dime el número 2 para hacer las operaciones  "))

print ("-----CALCULADORA-----")
print (f"SUMA {usuario_1} + {usuario_2} = {usuario_1 + usuario_2}")
print (f"RESTA {usuario_1} - {usuario_2} = {usuario_1 - usuario_2}")
print (f"MULTIPLICACION {usuario_1} * {usuario_2} = {usuario_1 * usuario_2}")
print (f"DIVISION {usuario_1} / {usuario_2} = {usuario_1 / usuario_2}")
