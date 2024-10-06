from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path ().absolute()) + "/fichero_texto.txt"

archivo = open(ruta, "a+") #con este comando hemos creado el "fichero_texto.txt" que aparece en el modulo 14

# a+: esto sirve para poder abrir o crear un archivo

"""
Lo que se ha visto en el apartado anterior, es la manera más segura de poder ver o abrir
un archivo. Es la manera más seguro y siempre va a funcionar.
"""

# Escribir
archivo.write("******* Soy un texto metido desde Python ******  \n")

# Cerrar el archivo
archivo.close()



# Abrir archivo
ruta = str(pathlib.Path ().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")
# r: es un permiso de lectura de archivo
"""
# Leer contenido
contenido = archivo_lectura.read()
print(contenido)  # Si solo imprimimos el contenido me muestra en contenido que hay en el archivo "fichero_texto.txt"
for elemento in contenido:
    print(elemento)
    # Con el buble for lo que hacemos es mostrar cada uno de los elementos del archivo "fichero_texto.txt"
"""

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)  
"""
Si comentamos la parte de leer contenido e imprimir contenido, y ejecutamos lista, cuando 
imprimimos nos sale todo lo que esta en el fichero "fichero_texto.txt" en una lista, es 
decir, cada elemento o fila en dentro de la lista
"""
print("\n ---------------------------------------------------\n")
# Ahora vamos a recorrer cada uno de los elementos para poder meterlos en una lista
for frase in lista:
    print("- "+frase.upper())

for frase in lista:
    if not frase.isnumeric():
        print("- "+frase.upper())


for frase in lista:   # con esto vamos a convertir cada frase en una lista
    lista_frase = frase.split()
    print(lista_frase)
    #print("- "+frase.upper())

for frase in lista:   
    #lista_frase = frase.split()
    #print(lista_frase)
    print("- "+frase.center(20))
    
    
# Copiar
"""
ruta_original = str(pathlib.Path ().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path ().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva) # con esto copiamos la ruta a nuestro directorio
"""
"""
# Mover
ruta_original = str(pathlib.Path ().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path ().absolute()) + "/fichero_copiado_NUEVO.txt"
shutil.move (ruta_original, ruta_nueva)
"""

# Eliminar
import os
ruta_nueva = str(pathlib.Path ().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva) # con esto vamos a eliminar la ruta del archivo que hemos creado en el apartado anterior


# Comprobar si existe
import os.path
#print(os.path.abspath("./"))

if os.path.abspath("./") + "/fichero_texto.txt":
    print("El archivo existe")
else:
    print("El archivo no existe")