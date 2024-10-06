"""
EJERCICIO 10
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos 
han aprobado y cuantos han suspendido.

"""
print("Para saber la nota de 15 alumnos primero tienes que decirmelas")


aprobado = 0
suspenso = 0

for i in range(1, 5):
    nota = int(input(f"Dime la nota del alumno {i}: "))
    while nota <= 0 or nota > 10:
        print("Este número no es válido. Por favor, introduce una nota entre 1 y 10.")
        nota = int(input(f"Dime la nota del alumno {i}: "))
    if nota >= 5:
        aprobado += 1
    else:
        suspenso += 1

print(f"El número de alumnos aprobados es de: {aprobado}")
print(f"El número de alumnos suspensos es de: {suspenso}")




