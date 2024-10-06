# ------------------- BUCLE WHILE ----------------------

"""
Estructura de control que itera o repite la ejecuación de una 
seria de insturcciones tantas veces como sea necesario, 
hasta que deje cumplirse la condición. 

while condición:
    bloque de instrucciones
    actualización de contador

"""

'''
La diferencia con entre while y for es que for tiene un numero finito (Ej: range 5), y while 
se ejecuta mientras no se cumpla la condición deseada. 
'''


contador = 1

while contador <= 100:
    print (f"Estoy en el número: {contador}")
    contador += 1  #esto es lo mismo que "contador = contador + 1"

print("---------------------")

contador = 1
muestrame = str (0)

while contador <= 100:
    muestrame = muestrame + "," + str (contador)
    contador = contador + 1 

print (muestrame)


"""
Vamos hacer un ejemplo de una tabla de multiplicar donde el usuario va  
a poder elegir el número de tabla de multiplicar que quiere y lo vamos a
hacer

"""

print ("##### EJEMPLO #####")

numero_usurario= int (input ("¿De qué número quieres la tabla?: "))

if numero_usurario < 1:
    numero_usurario = 1

print (f" ### Table del {numero_usurario} ###")

contador = 1 
while contador <= 10:
    print(f"{numero_usurario} x {contador} = {numero_usurario * contador}")
    contador += 1 
else: 
    print("Tabla finalizada.")


print ("##### EJEMPLO 200 #####")

numero_usurario= int (input ("¿De qué número quieres la tabla?: "))

if numero_usurario < 1:
    numero_usurario = 1

print (f" ### Table del {numero_usurario} ###")

contador = 1 
total = 0

while contador <= 10:
    resultado = numero_usurario * contador
    print(f"{numero_usurario} x {contador} = {resultado}")
    total += resultado 
    contador += 1 
else: 
    print("El suma total es:", total)