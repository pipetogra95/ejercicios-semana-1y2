inventario={'carne':{'precio':4,'cantidad':4}}
def añadir_producto(inventario):
    while True:
            nombre_producto=input("Cuál es el nombre del producto a agregar?\n")
            if nombre_producto in inventario:
                print("El producto ya está en inventario\n")
                break
            else:
                while True:
                    try:
                        precio_producto=float(input("Cuál es el precio unitario del producto?\n"))
                        if precio_producto<=0:
                            print("Debe ser un número mayor a cero")
                        else:
                            break
                    except ValueError:
                        print("Debes ingresar números mayores a cero")
                while True:
                    try:
                        cantidad_producto=int(input("Cuál es la cantidad de unidades?\n"))
                        if cantidad_producto<=0:
                            print("Debe ser un número entero mayor a cero")
                        else:
                            inventario[nombre_producto]={'precio':precio_producto,'cantidad':cantidad_producto}
                            break
                    except ValueError:
                            print("Debes ingresar un número entero mayor a cero")
            break
def consultar_producto(inventario):
    consulta=input("Qué producto desea consultar?\n")
    if consulta in inventario:
        print(inventario[consulta])
    else:
        print("El producto no está en inventario")
def actualizar_precio(inventario):
    producto=input("Cuál es el producto que desea modificar?\n")
    if producto in inventario:
        while True:
            try:
                nuevo_precio=float(input("Escriba el nuevo precio para el producto\n"))
                if nuevo_precio<=0:
                    print("Debe ingresar un valor mayor a cero")
                else: 
                   inventario[producto]['precio']=nuevo_precio
                   print(f"El precio de {producto} ha sido actualizado")
                   break
            except ValueError:
                print("Debe ingresar números mayores a cero")
    else:
        print("No existe un producto con ese nombre")
def eliminar_producto(inventario):
    producto=input("Cuál producto desea eliminar del inventario?\n")
    if producto in inventario:
        del inventario[producto]
        print(f"{producto} ha sido eliminado exitosamente")
    else:
        print("No existe un producto con ese nombre")
def calcular_valor_total(inventario):
    calcular_producto = lambda prod: prod['precio'] * prod['cantidad']
    total = sum(calcular_producto(prod) for prod in inventario.values())
    print(f"El valor total del inventario es: ${total:.2f}")
def menu():
    while True:
        print("         Bienvenido          ")
        print("Qué desea realizar?")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4.Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        try:
            opcion=int(input("Escriba el número de la acción a realizar\n"))
            if opcion==1:
                añadir_producto(inventario)
            elif opcion==2:
                consultar_producto(inventario)
            elif opcion==3:
                actualizar_precio(inventario)
            elif opcion==4:
                eliminar_producto(inventario)
            elif opcion==5:
                calcular_valor_total(inventario)
            elif opcion==6:
                print("Salida con éxito")
                break
            else:
                print("Debe escoger una opción válida, entre 1 y 6")
        except:
            print("Solo utilice números del 1 al 6")
menu()        