"""
EJERCICIO 9
Hacer un programa que pida numero al usuario indefinidamente hasta meter el numero 
111 

"""
numero = int(input("Dime un numero del 1 al 111 y te dire si el numero elegido: "))

while numero != 111:
    print("No has acertado el numero")
    numero = int(input("Prueba con otro numero del 1 al 111: "))
    if numero == 111:
        print("Has acertado con el numero correcto. Enhorabuena!!")