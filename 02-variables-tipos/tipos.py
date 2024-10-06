nada = None
cadena = "Hola soy Julio Briones"
cadena = "Desarrollador web"
entero = 99
flotante = 4.2
booleano = True
lista = [10,20, 30, 100, 200]
tupla = ("master", "en", "pyton")
diccionario = {
    "nombre": "Julio",
    "apellido": "Briones",
    "curso": "master en python"}

rango = range (9)
dato_byte = b"Probando"
# TUPLA: lista de datos que no pueden cambiar.
# DICCIONARIO: me permite tener una clave y un valor.



# imprimir variable
print(dato_byte)

# mostrar el tipo de dato 
print(type(dato_byte))

# STR = strings = cadena de texto
# INT = entero
# FLOAT = número decimal
# BOOL = booleano = Verdadero o Falso
# LIST = lista de datos variados
# TUPLE = 
# DICT = 
# RANGE
# BYTE


print("--------------------")
julio = (10, 20, 30, 40, 50)
print(julio)
print(type(julio))


print("--------------------")
julio = [10, 20, 30, 40, 50]
print(julio)
print(type(julio))


print("-------------")
julio = ("julio", "es el más", "guapo")
print(julio)
print(type(julio))


print("-------------")
julio = {
    "julio" : "el mas grande", 
    "Briones" : "es el más", 
    "Morales": "guapo"}
print(julio)
print(type(julio))



# CONVERTIR DATOS
"""
Yo no puedo concatenar un tipo de dato a otro. Es decir, yo no puedo unir 
un tipo de dato STR y INT. Tiene que ser los 2 del mismo genero. Es por ello 
que, a continuación se va a mostrar la manera en la que podemos juntar estos 
datos.

"""
texto = "Hola soy un texto"
numerito = str(776)
print(type(numerito)) # aqui va decir que es un tipo de dato texto
# 776
# "776"

print (texto + " " + numerito)

numerito = int(776)
print (type(numerito)) # ahora hemos convertido el tipo de dato a númerito *int

numerito=float(776)
print(numerito)
print(type(numerito)) # aqui dice que es un tipo de dato *float


nombre = "julio tiene"
numero = 25
numero = str(25)
print(nombre + " " + numero)






