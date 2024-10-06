"""
#Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones

SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    intrucciones
else:  
    Otras instrucciones

"""


#Ejemplo 1
print ("####### EJEMPLO 1 #######")

color = "rojo"

if color == "rojo":
    print("Enhorabuena")
    print("El color es ROJO")
else:
    print("El color NO es ROJO")

# Hacemos un ejemplo cambiando el color para ver lo que pasa

color = "verde"

if color == "rojo":
    print("Enhorabuena")
    print("El color es ROJO")
else:
    print("El color NO es ROJO")


"""
Lo que podemos hacer es cambiar la variable fija de color que ponemos por un valor 
que el propio usuario puede elegir. Lo podemos hacer con los "input".
"""


# color = "verde"
color = input("Adivina cual es mi color favorito: ")
if color == "rojo":
    print("Enhorabuena")
    print("El color es ROJO")
else:
    print("Color incorrecto")

    
"""

# OPERADORES DE COMPARACIÓN 
== igual 
!= diferente
< menor que 
> mayor que
<= menor o igual que
>= mayor o igual que

# OPERADORES DE LOGICOS 
and Y 
or  O
!  negación
not  NO

"""


#Ejemplo 2
print ("\n####### EJEMPLO 2 #######")

# Vamos a crear un ejemplo para saber si un año es mayor a 2021

year = 2020

if year >= 2021:
    print("Estamos de 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")

# Vamos hacer el mismo ejemplo preguntando el año al operador



"""
Si ejecutamos lo siguiente sin cambiar todo a misma variable, entero o palabras 
(INT - STR), al ejecutar el comando nos va a salir error. Es por ello que, vamos a 
convertir la variable "year" en un entero.
"""


year = int(input("¿En que año estamos?: "))

if year >= 2021:
    print("Estamos de 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")

# Podemos hacer otro ejemplo.

#Ejemplo 3
print ("\n####### EJEMPLO 3 #######")

# Vamos a crear un ejemplo para saber si un año es mayor a 2021

year = int(input("¿En que año estamos?: "))

if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")




#Ejemplo 4
print ("\n####### EJEMPLO 4 #######")

# Los anidados es meter un "if" dentro de otro "if"
# Vamos hacer un pequeño programa que compruebe la mayoría de edad de una persona

nombre = "Julio Briones"
ciudad = "Madrid"
continente = "Europeo"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    if continente != "Europa":
        print("El usuario no es Europeo")
    else:
        print(f"Es Europeo y de {ciudad} ")
else:
    print(f"{nombre} NO es mayor de edad")



#Ejemplo 5
print ("\n####### EJEMPLO 5 #######")        

"""
Queremos hacer un pequeño script que cuando metamos un número em lo identfique con un 
día determinado de la semana

"""


dia = int (input("Introduce el dia de la semana: "))


if dia == 1:
    print("Es lunes")
else:
   if dia == 2:
    print ("Es martes")
   else:
       if dia == 3:
           print("Es miercoles")
       else:
           if dia == 4:
               print("Es jueves")
           else:
               if dia == 5:
                   print("Es viernes")
               else:
                   print("Es fin de semana")



"""
Esto método de "if" es un poco elegible en caso de que queremos comprobar un error o salgo algo mal. 
Vamos a ver ahora una forma de poder hacerlo más sencillo. Este el método el "ELIF"

"""


# METODO ELIF

if dia == 1: 
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Vamos a ver como hacer varias condiciones dentro de cada "if"

#Ejemplo 6
print ("\n####### EJEMPLO 6 #######")

# Vamos a ser un programa para ver si un persona esta en edad de trabajar o no

edad_minima= 18
edad_maxima= 65
edad_oficial= int (input("¿Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >=18 and edad_oficial<= 65:
    print("Estas en edad de trabajar!!")
else:
    print("No está en edad de trabajar")


"""
# OPERADORES DE LOGICOS 

    and Y 
    or  O
    !  negación
    not  NO

"""

#Ejemplo 7
print ("\n####### EJEMPLO 7 #######")

#Vamos a hacer una comparación para poder ver si un país se habla español

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!!")
else: 
    print(f"{pais} no es un pais de habla hispana")



#Ejemplo 8
print ("\n####### EJEMPLO 8 #######")

# vamos hacer un ejemplo para practicas con el operador de negación

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana!!")
else: 
    print(f"{pais} SI es un pais de habla hispana")


#Ejemplo 9
print ("\n####### EJEMPLO 9 #######")

# vamos hacer un ejemplo para practicar con el operador de comparacion. En este caso diferente

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana!!")
else: 
    print(f"{pais} SI es un pais de habla hispana")

