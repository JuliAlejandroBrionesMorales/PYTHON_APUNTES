# ---------------------- BUCLE FOR ---------------------------

"""
# FOR

for variable in elemento iterable (lista, rango, etc.)
    BLOQUE DE INSTRUCCIONES

Elemento iterable: es cualquier elemento que puede almacenar datos. 

"""

contador = 0 
resultado = 0

for contador in range (0, 5):
    print("voy por el "+ str(contador))

    resultado = resultado + contador 
    # otra forma de poner esto es "resultado += contador"
print(f"El resultado es {resultado}")

"""
Lo que hace es dar vueltas en la variable hasta terminar el rango que hemos seleccionado
"""


# EJEMPLO TABLAS DE MULTIPLICAR

print("\n####### Ejemplo #######")

numero_usuario = int(input ("¿De qué número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1
print (f"\n#### Tabla de multiplicar del número {numero_usuario} ####")

for numero_tabla in range (1,11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
    
else: 
    print ("Tabla finalizada")


# Ejemplo para poder cerra un bucle "break"

print("\n #### Ejemplo cerrar bucle ####")

numero_usuario = int(input ("¿De qué número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1
print (f"\n#### Tabla de multiplicar del número {numero_usuario} ####")

for numero_tabla in range (1,11):
    if numero_usuario == 45:
        print ("NO se pueden mostrar número prohibidos !!!")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else: 
    print ("Tabla finalizada")

# Para poder cerrar un bucle for entre medias solo tenemos que poner "break"
