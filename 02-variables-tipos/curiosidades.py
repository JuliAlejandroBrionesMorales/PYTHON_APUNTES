mi_texto = '"Master"'
mi_texto2 = "en \"Pthon\""
"""
Para poner entre comillas un texto podemos utilizar \"texto\" cuando se 
se tenga varias palabras.
Cuando se tengo solo una palabra, la manera de poner entre comillas ese
texto al imprirmir es poner este texto entre una comilla ' "texto" '
"""


texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

# La manera de saltar a la siguiente linea es mediante la función " n\ ":
texto_unido = mi_texto + " \n " + mi_texto2
print(texto_unido)

# La manera de meter una tabulación entre 2 texto es mediante " \t ":
texto_unido = mi_texto + " \t " + mi_texto2
print(texto_unido)

# La manera de borrar todo lo que salga detras de un texto es " \r ":
texto_unido = mi_texto + " \r" + mi_texto2
print(texto_unido)