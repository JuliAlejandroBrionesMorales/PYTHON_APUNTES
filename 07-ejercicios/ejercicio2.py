"""
EJERCICIO 2
Escribir un scripts que nos muestre por pantalla todos los numeros pares del 
1 al 120

"""
print ("EJEMPLO WHILE")
contador = 2

while contador <= 120:
    print(f"vamos por el {contador}")
    contador += 2
print ("Trabajo finalizado")
 
print("----------------------")

# Tambien los podemos hacer con el bucle "for"
print("EJEMPLO FOR")

contador = 1

for contador in range (1,121): 
    if contador %2  == 0:
        print (contador)
else: 
    print("Trabajo finalizado")
