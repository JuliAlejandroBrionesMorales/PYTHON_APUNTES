"""
EJERCICIO 7
Hacer un programa que muestre todos los números impares entre dos número que decida 
el usuario

"""

numero1= int(input("Elige el primer número: "))
numero2= int(input("Elige el segundo numero: "))

numero3= numero1 +1

comprobacion = numero1 % 2
if comprobacion == 0:
    print("El primer numero es par")  
    numero1 =numero1+1
    while numero1<= numero2:
        print(numero1)
        numero1+=2
else:
    print("El primer numero es impar")
    while numero1 <= numero2:
            print(numero1)
            numero1+=2