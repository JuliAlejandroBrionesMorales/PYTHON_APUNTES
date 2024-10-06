"""
EJERCICIO 5
Hacer un programa que muestre todos los números entre 2 numeros que diga el usuario

"""
print("....EJEMPLO WHILE.....")

numero_1= int(input("Dime el numeró 1 a partir del cual quieras ver los números: "))
numero_2= int(input("Dime el número 2 hasta donde quieres ver los numero medios: "))

if numero_1  < numero_2:
    while numero_1 <= numero_2:
        print(numero_1)
        numero_1 = numero_1 + 1
    else: 
        print("Trabaja Finalizado")
else: 
    print("El numero 1 debe ser menor al numero 2")


print("---EJEMPLO FOR---")

numero_1= int(input("Dime el numeró 1 a partir del cual quieras ver los números: "))
numero_2= int(input("Dime el número 2 hasta donde quieres ver los numero medios: "))

if numero_1 < numero_2:
    for contador in range (numero_1, (numero_2+1)):
         print(contador)
else: 
       print("El numero 1 debe ser menor al numero 2")

