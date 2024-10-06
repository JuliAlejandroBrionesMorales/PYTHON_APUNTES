"""
Una variable es un contenedor de información que dentro 
guardará un dato, se pueden crear muchas variables y que
cada una tenga un dato distinto.
"""
# Crear variables y asignarles un valor
texto="Máster en Python"
texto2 = "con Julio Briones"
numero = 45
decimal = 6.7

# Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

#También podemos cambiar el valor de la variables poniendo 
# el mismo nombre de la variable pero poniendo otro dato en la 
# variable"

print("------------------------------------")

# Sustituir el valor de algunas variables / reasignar valores
numero = 55
decimal = 2.2
print(numero)
print(decimal)

print("------------------------------------")

# CONCATENACIÓN
# concatener es unir dos variables o más en una sola línea 
nombre= "Julio"
apellidos= "Briones"
web = "juliobriones.es"

print(nombre + " "+ apellidos + " - " + web)

print(f"{nombre} {apellidos} - {web}")

print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)



