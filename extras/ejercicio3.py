# Escriba un programa que consulte al usuario por una oración y comente al usuario  
# cuántas veces aparecen todas las vocales considerando minúsculas, mayúsculas y  
# acentos.

oracion = input("Ingrese un oracion:").lower()
letra_buscada ="a"
cantidad_a = 0
cantidad_e = 0
cantidad_i = 0
cantidad_o = 0
cantidad_u = 0

for letra in oracion:
    if(letra == 'a' or letra == 'á'):
        cantidad_a += 1
    elif(letra == 'e' or letra == 'é'):
        cantidad_e += 1
    elif(letra == 'i' or letra == 'í'):
        cantidad_i += 1
    elif(letra == 'o' or letra == 'ó'):
        cantidad_o += 1
    elif(letra == 'u' or letra == 'ú'):
        cantidad_u += 1

print("Cantidad de veces que aparece la letra 'a':", cantidad_a)
print("Cantidad de veces que aparece la letra 'e':", cantidad_e)
print("Cantidad de veces que aparece la letra 'i':", cantidad_i)
print("Cantidad de veces que aparece la letra 'o':", cantidad_o)
print("Cantidad de veces que aparece la letra 'u':", cantidad_u)

