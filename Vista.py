import Controller as ctr



print("Bienvenido al sistema de gestion de productos")
flag = True

while flag:
    try:
        print("Para resgiatrar un producto digite 1")
        print("Para consultar todos los producotos figite 2")
        print("Para actualizar un producto presione 3")
        print("Para eliminar un producto presione 4")
        print("Para consultar un producto por ID presione 5")
        print("Para consultar un producto que contenga en el nombre alguna cadena de caracteres presione 6")
        print("Para consultar un producto de una categoria especifica presione 7")
        print("Para consultar un producto por ranngo de precio presione 8")
        print("Para salir del programa presione 9")
        opc = int(input("Digite la opcion: "))


        if opc == 1:
            ctr.crearRegistro()
        elif opc == 2:
            print("Consultar todos los productos")
            ctr.consultarProductos()
        elif opc == 3:
            print("Actualizar producto")
            ctr.actualizarProducto()
        elif opc == 4:
            print("Eliminar producto")
            ctr.eliminarProducto()
        elif opc == 5:
            print("Consultar producto por ID")
            ctr.consultarProductoId()
        elif opc == 6:
            print("Consultar producto por nombre")
            ctr.consultarProductoNombre()
        elif opc == 7:
            print("Consultar producto por categoria")
            ctr.consultarProductoCategoria()
        elif opc == 8:
            print("Consultar producto por rango de precio")
            ctr.consultarProductoRangoPrecio()
        elif opc == 9:
            print("Gracias por usar el sistema")
            flag = False
            break

    except ValueError:
        print("Error, solo se permiten numeros enteros")
        continue