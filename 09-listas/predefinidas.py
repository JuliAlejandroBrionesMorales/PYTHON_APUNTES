cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar una lista
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Julio Briones") #insertar al final de la lista
cantantes.insert(1, "Eduardo Camavinga") # insertar en el indice 1
print(cantantes)

# Eliminar elementos
cantantes.pop(1) # Eliminamos el cantante en el índice 1
cantantes.remove ('Bad Bunny') # Con remove eliminamos un nombre en concreto
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse () # reverse te permite dar la vuelta a una reverse
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes) # con "in" podemos buscar un elemento dentro de una lista
print("\n")


# Contar elementos
print(cantantes)
print(len(cantantes))
print("\n")


# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))


# Conseguir indice
print(cantantes.index ("Drake"))
print("\n")

# Unir listas
cantantes.extend(numeros)
print(cantantes)