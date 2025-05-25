#El usuario ingresa un número entero positivo y el programa calcula la suma de sus dígitos.

numero = int(input("Ingrese un número: "))
suma = 0
while numero > 0:   
    digito = numero % 10
    suma += digito
    numero //= 10 
print("La suma de los dígitos es:", suma)
   