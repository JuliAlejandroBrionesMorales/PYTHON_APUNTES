"""
EJERCICIO 4.
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleando, 
y que imprima un mensaje según el tipo de dato de cada variable
"""
def TraducirTipo(tipo):   # con esta función traducimos el tipo de dato a algo más leíble
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "ENTERO"
    elif tipo == bool: 
        result = "BOOLEANO"
    return result


def comprobarTipado (dato, tipo): # con esta función vamos comprobar el tipado de dato
     test = isinstance(dato, tipo)
     result = ""

     if test: # esto se hace en caso de que el test sea verdadera, pues se imprime lo de abajo
        result = f"Este dato es del tipo {TraducirTipo(tipo)}"
     else:
        result = "El resultado de dato no es correcto"

     return result 


mi_lista = ["hola mundo", 77]
titulo =  "Master en Python"
numero = 22
verdadero = True

print(comprobarTipado(mi_lista, list)) # con esto comprobamos si mi  lista es del tipo lista
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))


    