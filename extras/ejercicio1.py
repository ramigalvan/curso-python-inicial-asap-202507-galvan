
continuar = True 
while(continuar):
    numero = int(input("Ingrese un numero: "))
    print(f"el numero {numero} es {'par' if (numero % 2 == 0) else 'impar'}")
    decision =  str(input("Desea continuar?  S/si o N/no: ")).lower()
    if(decision != 'si' and decision != 's'):
        continuar = False


