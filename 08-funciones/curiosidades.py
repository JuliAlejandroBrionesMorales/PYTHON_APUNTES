
def mi_funcion():
    print("Hola que tal")

def mi_segunda_funcion():
    print("Hola que tal 2")

nombre= "Julio"
apellido = "Briones"

print("Hola mundo")
print(f"Bienvenido {nombre}")

mi_funcion ()
mi_segunda_funcion ()
print("\n")

#el profesor nos recomienda que pongamos simpre la función arriba del todo
#la segunda recomendación del profesor es que quitemos el print de la función y utilizamos "return", y quedaría de la siguiente manera
print("------------------------")
def mi_funcion():
    return "Hola que tal" 

def mi_segunda_funcion():
    return "Hola que tal 2" 

nombre= "Julio"
apellido = "Briones"

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(mi_funcion ())
print(mi_segunda_funcion ())


print("\n")
# lo bueno de hacer las cosas con funciones es que podemos añadir cosas a las funciones. 
# en el siguiente ejemplo añadimos "nombre" y "apellido" a las anteiores funciones
def mi_funcion():
    return "Hola que tal" + nombre

def mi_segunda_funcion():
    return "Hola que tal 2" + apellido

nombre= "Julio"
apellido = "Briones"

print(mi_funcion ())
print(mi_segunda_funcion ())


# Es importante tener en cuenta, que las variables deben estar definidas antes de imprimir la función
# Es recomendable establecer las variables de fuera como parámetros de la función para poder unificar todo en la función
# En el siguiente ejemplo se muestra como convertir esas variables en funciones
print("\n Ejemplo de como pasar de variables a parámetros")
def mi_funcion(nombre):
    return "Hola que tal" + nombre

def mi_segunda_funcion(apellido):
    return "Hola que tal 2" + apellido

nombre= "Julio"
apellido = "Briones"

print(mi_funcion (nombre))
print(mi_segunda_funcion (apellido))


print("-----------------------------------")
#Ejemplo de como quitar las variables globales y meterlas en los parámetros de la función
print("\n Ejemplo de como pasar de variables a parámetros")
def mi_funcion(nombre):
    return "Hola que tal" + nombre

def mi_segunda_funcion(apellido):
    return "Hola que tal 2" + apellido


print(mi_funcion ("Julio Alejandro"))
print(mi_segunda_funcion ("Briones Morales"))
