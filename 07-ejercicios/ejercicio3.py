"""
EJERCICIO 3
Escribir un programa que muestre los cuadrados (un número multiplicado por si mismo)
de los 60 primeros numeros naturales. Resolver con while y for.
    1 x 1 
    2 x 2 
    3 x 3
"""

print ("FOR")
cuadrado = 1

for cuadrado in range (1,61):
    resultado = cuadrado * cuadrado
    print(f"{cuadrado} * {cuadrado}= {resultado}")

    
else: 
    print("Cuadrados finalizados")

print("----------")

print("WHILE")

cuadrado = 1

while cuadrado <= 60:
    resultado = cuadrado * cuadrado
    print (f"{cuadrado}*{cuadrado}= {resultado}")
    cuadrado +=1
else: 
    print("Trabajo finalizado")