"""
EJERCICIO 5.

Crear una lista con el contenido de esta tabla:
ACCION   AVENTURA               DEPORTES
GTA      ASSINS                  FIFA 21
COD      CRASH                   PRO 21
PUGD     Prince of Persia        MOTO GP 21

Mostrar esta información ordenada (por ejemplo, primero la categoría acción, luego aventura y luego deportes)

"""

tabla = [
    {
        "categoría":"ACCION",
        "juegos": ["GTA", "Call of Duty", "PUGB"]
    },
    {
        "categoría":"AVENTURA",
        "juegos": ["ASSINS", "Crash Bandicoot", "Price of Persia"]
    },
    {
        "categoría":"DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"---------- {categoria['categoría']}---------- ")
    for juego in categoria['juegos']:
        print(juego)