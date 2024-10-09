# ----------- PROGRAMACION ORIENTADA A OBJETOS -----------------------


# Definir una clase (moldde para crear más objetos de este tipo)
# (Coche) con características similares

from curses import color_content
from ipaddress import collapse_addresses


class Coche:
    
    # Atributos o propiedades (variables)
    # Características del coche
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    # Método, son acciones que hace le objeto (coche) (funciones)
    def setColor (self, color):
        self.color = color
        
    def getColor (self):
        return self.color
    
    def setModelo (self, modelo):
        self.modelo = modelo
    
    def getModelo (self):
        return self.modelo
    
    def acelerar (self):
        self.velocidad += 1
    
    def frenar (self):
        self.velocidad -= 1
        
    def getVelocidad (self):
        return self.velocidad

# fin definición clase
    
# Crear objetos / Instaciar la clase
coche = Coche ()
print("COCHE 1:")



# -------------- METODO GET AND SET -----------------
'''
Es la opción de meter funciones para poder cambiar atributos de tu coche mediante set (meter cosas nuevas)
y mediante get (obtener es nuevo valor)
'''

coche.setColor ("amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

coche.frenar()


print("Velocidad actual: ", coche.getVelocidad())

print("=========================================")


# --------------- CREAR MÁS OBJETOS -----------------------
coche2 = Coche()

coche2.setColor ('Verde')
coche2.setModelo ('Gallardo')

print("COCHE 2:")
print(coche2.getColor())
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))