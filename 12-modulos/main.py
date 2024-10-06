"""
MODULOS
Son funcionalidades ya hechas para reutilizar.
En python hay muchos modulos, que los puedes consultar en el siguiente enlace:
https://docs.python.org/3/library/math.html#module-math 

Podemos conseguir modulos que ya vienen en el lenguaje (modulos en internet) 
y también podemos crear nuestro modulos. 
"""


# Importar modulo propio (mimodulo.py)
import mimodulo

print(mimodulo.holaMundo("Julio Alejandro Briones Morales"))

print(mimodulo.calculadora(3, 5, True))


"""
Lo que te permite hacer una hoja con las funciones y clases es poder llevar estas funciones 
donde quieras, y solo sera necesario invocar (con import) la función para poder acceder a los elementos
que lo componen. 
Es una manera de poder tener tu codigo más limpio y que no se vea tan engoroso.
"""

print("\n")


# Si solo quiero importar una función de mi modulo hacemos lo siguiente
from mimodulo import  holaMundo
print(holaMundo("Julio Briones"))


"""
Tenemos otra forma de poder utilizar todas las funciones de mi archivo sin tener que invocar todo el rato el archivo
donde guardo las funciones[Ej: print(mimodulo.calculadora(3,5,True)]. Y lo podemos hacer de la siguiente manera: 
"""

from mimodulo import *

print(holaMundo("Eduardo Briones"))
print(calculadora(3,5,True))




# MODULO DE FECHAS
import datetime


print(datetime.date.today())  #podemos sacar la fecha del día de hoy

fecha_completa = datetime.datetime.now () # Cuando imprimimos esto nos da la fecha completa con hora, minutos, segundo....

print(fecha_completa)
print(fecha_completa.year) # cuando solo quiero mostrar el año 
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y,%H:%M:%S") #esto lo hemos sacado de la pagina con los datos de los módulos
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp()) #timestamp: sirve para poder sacar el tiempo en units
print(datetime.datetime.now().time()) # time: nos muestra el tiempo en otro formato

# Todo lo podemos ver en documentación de los módulos




# MODULO MATEMATICAS
import math

print("Raiz cuadrada de 10: ", math.sqrt(10)) # sqrt: raiz cuadrada de un numero

print("Numero pi: ", float(math.pi))

print("Redondear: ", math.ceil(6.78643)) # ceil: te permite redondear el numero a la alta

print("Redondear: ", math.floor(6.78643)) # floor: te permite redondear el numero a la baja


# MODULO RANDOM
# permite sacar numeros aleatorios
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67)) #radint: te permite sacar un numero aleatorio entre un rango determinado




