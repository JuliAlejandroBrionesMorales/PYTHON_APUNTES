# Importar modulo
from itertools import product
import sqlite3

# conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT, 
    precio int(255)  
)""")

# Guardar cambios
#conexion.commit()

# Insetar datos
''' 
cursor.execute("INSERT INTO productos VALUES (null,'Segundo producto', 'descripcion de mi producto', 550)")
conexion.commit()
'''

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("telefono movil", "Buen teléfono", 140),
    ("placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300), 
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio=778 WHERE precio=80")

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
print(cursor)

productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo:",producto[1])
    print("Descripción:",producto[2])
    print("Precio:",producto[3])
    print("\n")


cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone() # sacar el primer producto de la consulta
print(producto)


# cerrar conexión
conexion.close()