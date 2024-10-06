"""
DICCIONARIOS:
Un tipo de dato que almacena un conjunto de datos. 
En formato clave > valor.
Es pareceido a un array asociativo o un objeto json

"""

persona = {
 "nombre": "Victor",
 "apellidos": "Robles",
 "web": "victorroblewed.es"
}

print(type(persona))
print(persona) #mostramos el diccionario entero
print(persona["apellidos"]) # mostramos el apellido a traves del índice
print(persona["web"]) 

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email':'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos) #mostramos todo el diccionario
print(contactos[0]['nombre']) # seleccionamos el nombre dentro del indice 0

contactos[0]['nombre']= 'Antoñito' # cambiamos el nombre del indice 0
print(contactos[0]['nombre']) #imprimos el nombre del indice 0

print("\nLista de contactos: ")
print("-----------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}") # Con esto mostramos el nombre de cada uno de los contactos
    print(f"Email de contacto: {contacto['email']}") # Con esto mostramos el email de cada uno de los contactos
    print("-----------------")