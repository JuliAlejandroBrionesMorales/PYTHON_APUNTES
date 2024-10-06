# SET es un tipo de dato, para tener una colección de valores, pero no tiene ni indice ni orden

personas = {
 "Victor", 
 "Manolo",
 "Francisco"
}

personas.add("Paco") # De esta forma añadimos elemento en SETS
personas.remove("Francisco") # Eliminar un elemento del SETS

print(type(personas))
print(personas)

# Es preferible utlizar una lista antes que un sets
