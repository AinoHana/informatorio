
#Establecemos una lista vacía para almacenar los números primos
numeros_primos = []

#establece el rango de números a comprobar (1 a 1000) y el bucle lo recorre
for numero in range(1, 1001):
    if numero <= 1:
        es_primo = False #1 no es primo
    else:
        es_primo = True #Todos son primos hasta probar lo contrario
      
       #Comprueba si es primo al dividirlo y ver si el resto es 0, si lo es no es primo
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break #salir del bucle

#Si es primo, lo añade al final de la lista
    if es_primo:
        numeros_primos.append(numero)

print("Los números primos entre 1 y 1000 son:")
print(numeros_primos)
# El código encuentra todos los números primos entre 1 y 1000 y los imprime en una lista llamada numeros_primos.
  