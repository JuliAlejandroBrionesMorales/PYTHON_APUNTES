"""
Ejercicio 1.
Hacer un programa que tenga una lista de 8 numeros y haga lo siguiente: 
- Recorrer la lista y mostrarla
- Hacer una función que recorra las listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostralar su longitud
- Buscar algún elemento (que el usuario pida por teclado)
"""

lista = [1,3,5,6,8,44,10,65]

# 1. recorrer lista y mostrarla
for num in lista:
    print(num)
print("\n")

# 2. Crear función recorra lista y devuelva un string
def mostrar_lista (numeros):
    resultado = ""

    for elemento in numeros:
        resultado += "Elemento: "+ str(elemento)
        resultado += "\n"
    return resultado 

print(mostrar_lista(lista))



# 3. ordenar lista y mostrarla
lista.sort()
print(mostrar_lista(lista))
print("\n")

# 4. longitud de lista
longitud_lista = len(lista)
print(longitud_lista)


# 5. Buscar elemento solicitado por operador

try:
    busqueda = int(input("Introduce un numero: "))

    comprobar = isinstance(busqueda, int)
    
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce un numero: "))
    else:
        print(f"Has introducido el: {busqueda}")

    print(f"#### Buscar en la lista el número {busqueda} ####")


    search = lista.index(busqueda)
    print(f"El numero buscado existe en la lista, y es el índice: {search}") 
except:
    print("El numero no esta en la lista")

 