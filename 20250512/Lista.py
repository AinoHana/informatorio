numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Lista comprehension, elementos potenciados por sí mismos
potenciados = [i ** i for i in numbers]
print(potenciados)

lenguajes_p = ['java', 'python', 'go', 'rust']
leng_corregidos = [leng[0].upper() + leng[1::] for leng in lenguajes_p]
print(leng_corregidos)