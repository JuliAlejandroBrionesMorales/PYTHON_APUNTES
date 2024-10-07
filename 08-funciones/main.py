# ------------------ FUNCIONES --------------------------

"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la función tantas 
veces como sea necesario.

En otros lenguajes la palabra función es "funtion" pero en 
python es "def",

def nombreDeMiFunción (parametros): 
    #BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFunción (mi_parametro) 
nombreDeMiFunción (mi_parametro) 

"""

# Ejemplo 1
print("#### Ejemplo 1 ####")

def muestraNombres():
    print("Julio")
    print("Alejandro")
    print("Eduardo")
    print("Manolo")
    print("Jose")
    print("Laura")
    print("Ester")
    print("\n")

# Invocar función (ejecutar función)
muestraNombres()



# Ejemplo 2: parámetros
print("#### EJEMPLO 2 ####")

nombre ="Julio Briones"

def mostrartuNombre (nombre):
    print(f"Tu nombre es: {nombre} ")

mostrartuNombre (nombre)


print("--------------")
#Ahora metemos los parametros dentro de la función

def mostrartuNombre (nombre):
    print(f"Tu nombre es {nombre}")

mostrartuNombre ("Julio Briones")
mostrartuNombre ("Manolito")
mostrartuNombre ("Pepito")

print("--------------")
#ahora lo vamos hacer con el nombre que sea el que usuario quiera

def mostrartuNombre (nombre):
    print(f"Tu nombre es {nombre}")

nombre =input("introduce tu nombre: ")
mostrartuNombre (nombre)

"""
Un parametro es un dato que yo paso desde fuera a la función. De esto modo puedo 
parametrizar la funcionalidad que hay dentro de una función

"""
 
# Vamos hacer un ejemplo para poder meter 2 parámetros 

def mostrartuNombre (nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad >= 18:
        print ("Y eres mayor de edad")
    

nombre =input("introduce tu nombre: ")
edad= int(input("¿Cual es tu edad?:"))
mostrartuNombre (nombre, edad )

'''
Cuando creamos un "input" siempre es del tipo "str", por lo que si queremos un valor numérico, 
es necesario que lo transformememos a int.
'''

print (".........------------------...........")





# Ejemplo 3

print("##### EJEMPLO 3 #####")

# Vamos hacer la tabla de multiplicar del 1 al 10 de cualquier numero que pongamos en el parámetro de la función

numero = int(input("Dime de que número quieres la tabla de multiplicar: "))

def tabla (numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    for contador in range (11):
        operacion = numero*contador
        print(f"{numero} * {contador} = {operacion}")
    
    print("\n")

tabla (numero)

# Ejemplo 3.1
print("-------------------------")
for numero_tabla in range (1, 11):
    tabla(numero_tabla)
#Aqui hemos hecho la tabla de multiplicar del 1 al 100 pero de 1 al 10 para cada numero. 
    




# Ejemplo 4
    
print("##### EJEMPLO 4 - PARAMETROS#####")

# Parámetros opcionales
def gestEmpleado (nombre, DNI = False):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if DNI != False:
        print(f"DNI: {DNI}")

gestEmpleado ("Julio Briones", "D213")


"""
Podemos eliminar el segundo parametro metiendo ciertas restricciones en la función.

Por ejemplo, si el operador no pone el dni, podemos poner que se se elimine ese parámetro o que sea una palabra o 
número determinado

"""


print("\n ##### EJEMPLO 5 - RETURN #####")
# Ejemplo 5: return o devolver datos

def saludame (nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame ("Julio Briones"))

# El "return" se utiliza en funciones para devolver un valor. Es decir, nos permite sacar una valor de dentro la función hacia afuera.
# El "return" es como una especio de print que se hace de dentro hacia afuera.


# Ejemplo 6
print("\n ##### EJEMPLO 6 #####")

def calculadora (numero1, numero2, basicos = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    
    if basicos != False: 
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(56,5))

print("\n Ejemplo con parámetro TRUE")
print(calculadora(56, 5, True))


# Ejemplo 7:
print("\n ##### EJEMPLO 7 - FUNCIONES DENTRO DE FUNCIONES #####")

#Vamos a utlizar funciones dentro de otras funciones

def getnombre (nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getapellidos (apellidos):
    texto= f"Los apellidos son: {apellidos}"
    return texto

def devuelvetodo (nombre, apellidos):
    texto = getnombre (nombre) + "\n" + getapellidos(apellidos)
    return texto

print(devuelvetodo("Julio Alejandro", "Briones Morales"))


# Ejemplo 8: Funciones Lambda
print("\n ##### EJEMPLO 8 #####")

"""
Una función "LAMBDA" es una función anonima. Una función anonima es una función que no tiene nombre o un nombre concreto. 
No es necesario definirla con el def. Son funciones que sirven para funciones simples y pequeñitas que puede llegar a ser 
repetitivas. 
"""

dime_el_year = lambda year: f"El año es {year*50}"

print(dime_el_year(2024))




