"""
EJERCICIO 8
¿Cuanto es el X por cierto de X numero?
        Ej: 20 % de 15'

"""

numero = int(input("Dime el numero: "))
porcentaje = int(input("Dime el porcentaje que quieres del numero: "))

print(f"El {porcentaje} % de {numero} es {(numero * porcentaje)/(100)}")


print("-------------------")

print("FORMA 2 de hacerlo")
print("Si quieres saber el porcentaje 'y' de 'x' numero es necesario fijar los valores")

numero = int(input("Dime el numero elegio: "))
porcentaje= int(input("Ahora dime el porcentaje que quieres de ese numero: "))

print(f"El {porcentaje}% de {numero} es de {(numero * porcentaje )/(100)}")



