# Ejercicio 4
# Escriba un programa que solicite la edad de la persona e imprima todos los años que la
# persona ha cumplido.


edad_valida = False 
edad = 0

def ingresar_edad():
    global edad_valida, edad

    while(not edad_valida):
        edad = int(input("Ingrese su edad:"))
        if(edad <= 0):
            print("Edad invalida. Intente de nuevo.")
        else:
            edad_valida = True

def imprimir_anios():
    i = 1
    while(i <= edad):
        print(f"Usted ha cumplido {i} {'año' if i == 1 else 'años'}")
        i += 1

ingresar_edad()
imprimir_anios()


