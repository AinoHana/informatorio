#se ingresa por pantalla una cadena y se debe revertirla
#No se puede usar reverse, ni [::-1]

cadena = input("Ingrese una palabra u oración:")
invertida = ""

for letra in cadena:
    invertida = letra + invertida
    print(invertida)

if cadena == invertida:
    print("La cadena es un palíndromo")
else:
    print("La palabra no es palíndromo.")