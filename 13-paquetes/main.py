# ------------------ PAQUETES -------------------------

"""
Un paquete es un conjunto de modulos.
Por ejemplo si queremos hacer un programa, podemos crear diferentes paquetes con los modulos necesarios para poder 
hacer el programa.
"""
print("PROBANDO PAQUETES:")

# cuando ejecutamos un paquete Python general un carpeta de pycache (no debemos tocarla)

from mipaquete import pruebas
from mipaquete import herramientas

pruebas.probando ()
herramientas.nombreCompleto("Julio", "Briones")

# Los paquetes nos permiten mejorar la arquitectura de nuestra aplicación
# Una forma de abreviar la importación de paquetes es la siguiente "from mipaquete import pruebas, herramientas"

# Para poder instalar paquetes de Python: https://pypi.org/ 


