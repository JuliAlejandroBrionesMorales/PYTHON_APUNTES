"""
LISTAS (array)
Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un indice númerico.
"""

pelicula = "Batman"



# DEFINIR LISTA


peliculas = ["Batman", "Spiderman", "El señor de los anillos"] 
cantantes = list(('Tupac', 'Drake', 'Jeniffer Lopez')) # Otra forma de poder hacer una lista es con la función "list"
year = list (range(2020, 2050))
variada = ["Julio", 20, 4.4, True, "Texto"]


print(peliculas)
print(cantantes)
print(year)
print(variada)

"""
- "peliculas" -- cada una de las variables dentro de la lista se llaman por indices y se empieza a contar a partir del indice 0.
- "cantantes" -- cuando ponemos 2 parentesis en la función "list" convertimos esos valores en una tubla, es decir, que no se 
   pueden modificar y es una lista
"""



# INDICES
#Este ejemplo ilustra como cambiar el nombre de un indice dentro de una lista.

pelicula = "otra cosa"
peliculas [1]= "Gran torino"  # aqui lo que hemos hecho es cambiar el nombre de un indice. Cambio de "Spiderman" por "Gran Torino"
peliculas [2]= "Popeye" #Aqui hemos cambiado "el señor de los anillos" por "popeye"

print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(cantantes[0:1])
print(cantantes[0:3])
print(peliculas[1:])
print(peliculas[2:])
#Aqui lo que hemos hecho es sacar indice concretos de las listas
#Podemos sacar indices para poder cambiarlos o actualizarlos mendiante las llaves.



# AÑADIR ELEMENTOS A LISTA
cantantes.append ("Pablo Escobar") # Este elemento se añade al final de la lista
cantantes.append("Cristina Aguilera") # Este nuevo nombre también se añade al final de la lista
print(cantantes)
#Con el ".append" puedo añadir elementos al final de mi lista.



# RECORRER LISTA

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
      peliculas.append(nueva_pelicula) # con esto preguntamos al usuario peliculas para poder meterla en la lista peliculas


print("\n ************ LISTADO PELICULAS ************ ")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}") # con esto recorremos el listado peliculas y lo desglosamos 1 a 1





# LISTA MULTIDIMENSIONAL 
    # Es una lista dentro de otra lista, es decir, que tiene varias dimensiones
print("\n ************ Listado de contactos ************")
contactos = [
   [
      'Antonio',
      'antonio@antonio.com'
   ],
   [
      'luis',
      'luis@luis.com'
   ],
   [
      'Salvador',
      'salvador@salvador.com'
   ],
      ]

print (contactos) # mostramos lista entera
print(contactos [1]) #mostramos datos de luis
print(contactos [1][1]) #mostramos solo correo de luis
print("\n")

for contacto in contactos:
    for elemento in contacto:
        print(elemento)  # De esta manera sacamos el nombre, email uno a uno
    print("\n") # Con esto metemos el salto de linea por cada bloque de nombre/mail

#Luego con el bucle podemos hacer mil cosas como la siguiente: 
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento) # Con esto hemos añadido la palabra nombre y mail dentro de cada uno de los datos de la lista
    print("\n") # Con esto metemos el salto de linea por cada bloque de nombre/mail  
