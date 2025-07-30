# Tarea Python
# Hacer un sistema de facturación para una verdulería. Este sistema debe preguntar lo siguiente al cliente y calcular los precios.
# -Qué vas a comprar, cuanta cantidad, 
# -Preguntar qué más va a comprar, y repetir el ciclo hasta que el cliente no quiera más.
# -Al final debe mostrar el “ticket” con los ítems y sus precios. Y el total a pagar por toda la compra.
 
# Lo que necesitamos para hacerlo es lo siguiente:
# - while
# - input()
# - variable
# - lista
# - for/in

productos = [["banana", 5.60], ["pera", 2.60], ["manzana", 9.50]]
# la lista de productos originales deberia de ser: productos [ [producto, precio],[producto, precio],[producto, precio], ]
productos_comprados = []
# la lista de productos comprados deberia de ser:  [ [producto, cantidad], [producto, cantidad], [producto, cantidad] ]


# el usuario debe de poder elegir el producto segun el ID
# TODO el usuario debe de poder indicar la cantidad que quiere 
def comprar_producto():
    ver_productos()

    id_producto = int(input("Ingrese el id del producto que desea comprar:"))

    if(id_producto < 0 or id_producto >= len(productos)):
        print("ID de producto invalido.")
    else:
        cantidadValida = False
        while(not cantidadValida):
            cantidad = int(input("Ingrese la cantidad que quiere comprar:")) #controla el caso de que el usuario haya ingresado 0
            if(cantidad > 0):
                cantidadValida = True
            else:
                print("Cantidad invalida!!!. Ingrese un numero mayor a 0")

        producto_buscado = productos[id_producto]
        producto_existente = False

        for producto in productos_comprados:
            if(producto[0] == producto_buscado[0]):
                producto[1] += cantidad
                producto_existente = True
                break
        
        if(not producto_existente):
            productos_comprados.append([producto_buscado[0], cantidad])
        
        print("Producto agregado al carrito!")



def ver_productos(): 
    print("------Productos disponibles-------")
    for producto in productos:
        print("ID:", productos.index(producto) ,  "-", producto[0],  "- $", producto[1])

#deberia de poder ver el nombre, la cantidad, el precio unitario y un subtotal
def ver_productos_comprados():
    print("------Productos comprados-------")
    print("Producto ------- Cantidad ------ P.U --------- Subtotal")
    for producto in productos_comprados:
        nombre = producto[0]
        precio_producto = obtener_precio_producto(producto[0])
        cantidad_producto = producto[1]
        subtotal = precio_producto * cantidad_producto
        print(f"{nombre} {cantidad_producto} $ {precio_producto:.2f}  $ {subtotal:.2f}")

def obtener_precio_producto(nombre_producto):
    precio = 0
    for producto in productos:
        if(producto[0] == nombre_producto):
            precio = producto[1]
            break
    
    return precio

def calcular_totales():
    total = 0
    print("------Productos comprados-------")
    print("Producto ------- Cantidad ------ P.U --------- Subtotal")
    for producto in productos_comprados:
        nombre = producto[0]
        precio_producto = obtener_precio_producto(producto[0])
        cantidad_producto = producto[1]
        subtotal = precio_producto * cantidad_producto
        total += subtotal 
        print(f"{nombre} {cantidad_producto} $ {precio_producto:.2f}  $ {subtotal:.2f}")
    print("----------------------------------")
    print("Total de su compra:", total)


def finalizar_compra():
    if(len(productos_comprados) == 0):
        print("Gracias por su visita!")
    else:
        calcular_totales()
        print("Gracias por su compra")

def verificar_opcion(opcion): 
    match opcion:
        case 1:
            ver_productos()
        case 2:
            ver_productos_comprados()
        case 3:
            comprar_producto()
        case 4:
            finalizar_compra()
        case _:
            print("Opcion invalida!")

print("Bienvenido a la verduleria py")

opcion = -1
while(opcion != 4):
    opcion = int(input("\nOperaciones disponibles:" \
    "\n1-Ver productos" \
    "\n2-Ver carrito" \
    "\n3-Comprar Producto" \
    "\n4-Finalizar compra" \
    "\nIngrese una opcion:"))
    verificar_opcion(opcion)

