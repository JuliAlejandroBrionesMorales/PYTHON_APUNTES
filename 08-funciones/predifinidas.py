
nombre = "Julio Briones"

# FUNCIONES GENERALES
print(nombre)
print(type(nombre))


# DETECTAR TIPADO

comprobar = isinstance (nombre, int)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance (nombre, float):
    print("La variable no es un numero con decimales")



# LIMPIAR ESPACIO

frase = "     mi contenido     "
print(frase)
print(frase.strip())

# la función .strip lo que hace eleminar los espacio dentro de una frase



# ELIMINAR VARIABLES
year = 2023
print (year)
del year
#print(year)
# con la función "del" podemos eleminar una variable. Si le damos a imprimir no funciona



# COMPROBAR VARIABLES VACIAS

texto = " fff  "
if len (texto)<=0:
    print("La variable esta vacía")
else:
    print("La variable tiene contenido: ", len(texto) )

#"len" nos sirve para saber cuantos caracteres tienes una variable
    

# ENCONTRAR CARACTERES A PARTIR DEL INDICE

frase = "La vida es bella"
print(frase.find("vida"))
#en la respuesta nos dira que la palabra se encuentra a partir del caracter 3


# REEMPLAZAR PALABRAS EN UN STRING
nueva_frase = frase.replace ("vida","moto")
print(nueva_frase)


# MAYUSCULAS Y MINUSCULAS
print(nombre)
print(nombre.lower())  #miniscula
print(nombre.upper())  #mayusculas
#convertir palabras/variables en mayusculas o minisculas

