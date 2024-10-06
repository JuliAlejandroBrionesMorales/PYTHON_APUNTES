"""
EJERCICIO 2.    
Escribir un pograma que añada valores a una lista, mientras su longitud sea menor
a 120 y luego mostrar lista. 
Hacerlo tanto con while como con for
"""


print("##### Modelo con buble while ####")
lista = []

while len(lista) <=5 :
    numero_operador = input("Dime un numero que quieras añadir a la lista: ")
    lista += numero_operador
print(lista)
# Esta forma muestra como hacerlo con numeros escritos por el operador

print("##### \n Modelo con buble for ####")

coleccion = []

for contador in range (0,120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: "+ coleccion[contador])
print(coleccion)


print("####\n Modelo con bucle while #####")

lista = []
x = 0
while x < 120:
    lista.append(f"elemento - {x}")
    print("Mostrando el:"+ lista[x])
    x += 1

print(lista)

