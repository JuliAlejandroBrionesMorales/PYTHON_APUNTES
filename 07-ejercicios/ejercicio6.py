"""
EJERCICIO 6
Mostrar todas las tablas de multiplicar del 1 al 10. Mostrar el titulo de la tabla 
y luego las multiplicaciones del 1 al 10.  

"""

contador= 1
multiplicador = 1

while contador <=10:
    print(f"Tabla de multiplicar del {contador}")
    for multiplicador in range (1,11):
        print(f"{contador}*{multiplicador}= {contador * multiplicador}")
        multiplicador +=1 
    contador +=1
else: 
    print("Trabajo finalizado")