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
print(informatico.getLenguaje())

print("----------------------------------")