import sys 

# Convierte los argumentos pasados por consola a enteros
valor1 = int(sys.argv[1])
valor2 = int(sys.argv[2])
valor3 = int(sys.argv[3])

# Muestra si cada numero es par o impar
print(f"el primer valor es {'par' if (valor1 % 2 == 0) else 'impar'}")
print(f"el segundo valor es {'par' if (valor2 % 2 == 0) else 'impar'}")
print(f"el tercer valor es {'par' if (valor3 % 2 == 0) else 'impar'}")
