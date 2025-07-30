# Ejercicio 2
# Escriba un programa que consulte al usuario por una oración y comente al usuario
# cuántas veces aparece la letra “a”.

oracion = input("Ingrese un oracion:").lower()
letra_buscada ="a"
cantidad_a = 0

for letra in oracion:
    if(letra_buscada == letra):
        cantidad_a += 1

print("Cantidad de veces que aparece la letra 'a':", cantidad_a)

