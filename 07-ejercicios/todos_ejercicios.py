"""
EJERCICIOS 1.
    - Crear variables "pais" y "continenete"
    - Mostrar su valor en pantalla (imprimir)
    - Poner un comentario diciendo el tipo de dato
"""
'''
pais = 'peru'
continente = 'America'

print(pais)
print(continente)
print(type(pais))
'''


"""
EJERCICIO 2
Escribir un scripts que nos muestre por pantalla todos los numeros pares del 
1 al 120

"""
"""
contador = 2
while contador <=120:
    print(contador)
    contador += 2
else:
    print('Ahí tienes todos los números pares')
"""

"""
EJERCICIO 3
Escribir un programa que muestre los cuadrados (un número multiplicado por si mismo)
de los 60 primeros numeros naturales. Resolver con while y for.
    1 x 1 
    2 x 2 
    3 x 3
"""
"""
numero = 1
for numero in range (61):
    print(f'{numero} x {numero}= {numero * numero}')
    numero +=1
    
"""


"""
EJERCICIO 4

Pedir 2 numeros al usuario y hacer todas las operaciones básicas de una calculadora y 
mostrarlo por pantalla

"""
"""
numero1 = int(input ('Dime el primer numero para hacer tus operaciones: '))
numero2 = int(input ('Dime el segundo numero para hacer tus operaciones: '))

print(f'La multiplicación es \n {numero1} x {numero2} = {numero1*numero2}')
print('------------------------')
print(f'La división es \n {numero1} / {numero2} = {numero1/numero2}')
print('------------------------')
print(f'El resto es \n {numero1} % {numero2} = {numero1%numero2}')
print('------------------------')
"""


"""
EJERCICIO 5
Hacer un programa que muestre todos los números entre 2 numeros que diga el usuario

"""

"""
print('Vamos a sacar todos los numeros entre dos cifras elegidas por ti. Elige el rango que quieres.')
numero1 = int(input ('Dime el numero 1: '))
numero2 = int(input ('Dime el numero 2: '))

if numero1 > numero2:
    while numero2 < numero1:
        numero2 =numero2 +1
        print(numero2)
else:
    while numero1 < numero2: 
        numero1 = numero1 +1
        print(numero1)
"""


"""
EJERCICIO 6
Mostrar todas las tablas de multiplicar del 1 al 10. Mostrar el titulo de la tabla 
y luego las multiplicaciones del 1 al 10.  

"""

"""
print('TABLA DE MULTIPLICAR DEL 1 AL 10')
contador = 1
while contador <=10:
    print(f'Tabla de multiplicar del {contador}')
    for multiplicador in range (11):
        print(f'{contador} x {multiplicador} = {contador * multiplicador}')
        multiplicador +=1
    contador +=1   
else:
    print('HEMOS FINALIZADO CON TU PEDIDO')
"""


"""
EJERCICIO 7
Hacer un programa que muestre todos los números impares entre dos número que decida 
el usuario

"""



"""
EJERCICIO 8
¿Cuanto es el X por cierto de X numero?
        Ej: 20 % de 15'

"""
"""
numero = int (input('Elige tu numero: '))
porcentaje = int (input('Dimero el porcentaje que quieres que saquemos de tu numero: '))

porcentaje_numero = (numero *porcentaje)/100

print(f'El porcentaje del número elegido es: {porcentaje_numero}')
"""

"""
EJERCICIO 9
Hacer un programa que pida numero al usuario indefinidamente hasta meter el numero 
111 

"""

"""
numero  = int (input('Dime un numero entre el 0 y 111, a ver si es el que estoy pensando: '))
while numero != 111:
    numero = int(input ('El numero no es correcto. Sigue intentandolo: '))
else: 
    print('Es correcto. El número que estaba pensando es el 111') 
"""


"""
EJERCICIO 10
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos 
han aprobado y cuantos han suspendido.

"""

aprobado = 0
suspenso = 0

for i in range (1, 5):
   nota = int(input(f"dime la nota del alumno {i}: "))
   if nota <= 0: 
    print("Este numero no es valido por lo que tiene que volver a poner la nota entre 1 y 10")
    nota = int(input(f"dime la nota del alumno {i}: "))
    if nota >= 5:
            aprobado +=1
    else: 
            suspenso+=1

print(f"El numero de alumnos aprobados es de: {aprobado}")
      
print(f"El numero de alumnos suspensos es de: {suspenso}")