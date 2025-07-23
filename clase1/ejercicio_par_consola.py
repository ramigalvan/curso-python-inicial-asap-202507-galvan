# Solicita al usuario ingresar tres números enteros 
valor1 = int(input("Ingrese el primer numero "))
valor2 = int(input("Ingrese el segundo numero "))
valor3 = int(input("Ingrese el tercer numero "))

# Muestra si cada numero es par o impar
print(f"el primer valor es {'par' if (valor1 % 2 == 0) else 'impar'}")
print(f"el segundo valor es {'par' if (valor2 % 2 == 0) else 'impar'}")
print(f"el tercer valor es {'par' if (valor3 % 2 == 0) else 'impar'}")

