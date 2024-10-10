import clases

persona = clases.Persona()
persona.setNombre("Julio")
persona.setApellidos("Briones")
persona.setAltura("190cm")
persona.setEdad ("800 años")


print(f"La persona es:  {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("----------------------------------")

informatico = clases.Informático()
informatico.setNombre('Carlos')
informatico.setApellidos('Martinez')

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes)
print(informatico.caminar())
print(informatico.experiencia)


print("----------------------------------")

'''
Para este ejemplo de técnico de redes hemos podido ver como se aplica la herencia de una clase 
a otra, la manera en que podemos pasar los constructores de una clase a otra, y como podemos invocar
una funciones y clases de una documento a otro para poder hacer el código más sencillo.
'''

tecnico = clases.TecnicoRedes()
tecnico.setNombre ('Manolo Gate')

print(tecnico.auditorRedes, tecnico.getNombre(), tecnico.getLenguajes())