# ------------------ PAQUETES -------------------------

"""
Un paquete nos permite agrupar varios modulos. 
Por ejemplo si queremos hacer un programa, podemos crear diferentes paquetes con los modulos necesarios para poder 
hacer el programa.
"""

print("PROBANDO PAQUETES:")

'''
Cuando creamos el archivo _init_.py dentro la carpeta mipaquete, python entiendo que eso esa carpeta es 
un paquete, y dentro del la carpeta de mipaquete podemos meter tantos módulos como queramos. En nuestro 
caso, hemos credo herramientas.py y pruebas. py  
'''

# Cuando ejecutarmos un paquete en Python, por lo general se crea una carpeta de pycache (NO TOCARLA)


# Importamos paquetes
from mipaquete import pruebas
from mipaquete import herramientas
# Otra forma de importar es from mipaquete import pruebas, herramientas

# Utilizamos los modulos que estamos utilizando. 
pruebas.probando ()
herramientas.nombreCompleto("Julio", "Briones")


# Los paquetes nos permiten mejorar la arquitectura de nuestra aplicación
# Para poder instalar paquetes de Python: https://pypi.org/ 


