"""
EJERCICIO 3:
Programa que comprueba si una variable esta vacia y si está vacia, rellenarla con texto en minúsculas y mostrarlo
en mayúsculas.
"""

texto = ""

if len(texto.strip()) <= 0: # con strip elimimos los espacio de la cadena de texto
    texto  = "hola soy un texto en minusculas"
    print(texto.upper()) # establecemos texto en mayusculas
else:   
     print(f"La variable tiene contenido {texto}")








