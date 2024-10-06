"""
- Variable Locales: se define dentro de la función y no se puede utilizar fuera de ella, solo están disponibles dentro. 
                    A no ser que hagamos un return
- Variables Globales:son las que se declaran fuera de una función y estan disponibles dentro y fuera de ellas. 

"""

# Variable Global

print("EJEMEPLO PARA DIFERENCIAR VARIABLES LOCALES Y GLOBALES")
print("\n")
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres "

print(frase)

def holamundo():
    frase = "Hola mundo"
    print("Dentro de la función")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "juliobriones.com"
    print("Dentro: ", website)

    return "Dato devuelto " + str(year)

print(holamundo())
print("Fuera: " ,website)

"""
Para poder sacar una variable de dentro hacia fuera tenemos que sacar la variable de la función con "return" y para poder convertir 
una variable local en una variable global tenemos que utilizar función "global" dentro de la función
"""


