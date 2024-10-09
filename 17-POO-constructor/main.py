from coche import Coche

carro = Coche ("Morado", "Renault", "Clio", 150, 200, 4)
carro1 = Coche ("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche ("Azul", "Citroen", "Xsara", 180, 180, 4)
carro3 = Coche ("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())


# ------------------ DETECTAR TIPADO --------------------
carro3 = 'Aleatorio'
if type (carro3) == Coche:
    print("Es un objeto correcto!!")
else:
    print("No es un objeto")
    

# ------------------ VISIBILIDAD --------------------
'''
Para poder visualizar un atributo privado, tenemos que crear una función de Get
para poder sacar este atributo privado como un atributo de la clase.
'''
print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())