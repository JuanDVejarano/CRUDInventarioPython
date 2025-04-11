import sqlite3 as db
from prettytable import PrettyTable

def consultarCategoria():
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM categoria"
    resultado = cursor.execute(instruccionSQL)
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                """.format(dato[0], dato[1]))
    conn.close()

def ValidarNombre(nombre):
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Producto WHERE nombre = ?"
    resultado = cursor.execute(instruccionSQL, (nombre,))
    print(resultado.fetchone())
    if resultado.fetchone() is not None:
        print("El nombre del producto ya existe")
        conn.close()
        return True
    else:
        conn.close()
        return False
    
def ValidarCategoria(categoria):
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM categoria WHERE id = ?"
    resultado = cursor.execute(instruccionSQL, (categoria,))
    if resultado.fetchone() is not None:
        conn.close()
        return False
    else:
        conn.close()
        return True

def validarIdPrducto(idf):
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Producto WHERE id = ?"
    resultado = cursor.execute(instruccionSQL, (idf,))
    if resultado.fetchone() is not None:
        conn.close()
        return False
    else:
        conn.close()
        return True

def crearRegistro():
    nomf = input("Digite el nombre del producto: ")
    preciof = int(input("Digite el precio: "))
    cantf = int(input("Digite la cantidad: "))
    consultarCategoria()
    categf = input("Digite el id categoria: ")

    #controlar contenido datos
    if (len(nomf) > 0 and len(categf) > 0 and cantf > 0 and preciof > 0):
        #validar que no exista el nombre del producto ya en la base de datos
        if(ValidarNombre(nomf)):
            print("Error, el nombre del producto ya existe en la base de datos")
            return
        elif(ValidarCategoria(categf)):
            print("Error, la categoria no existe en la base de datos")
            return
        else:
            conn = db.connect("Inventario.db")
            cursor = conn.cursor()
            instruccionSQL = "INSERT INTO Producto (nombre, precio, cantidad, categoria_id) VALUES (?, ?, ?, ?)"
            cursor.execute(instruccionSQL, (nomf, preciof, cantf, categf))
            conn.commit()
            conn.close()
            print("El registro se creo exitosamente")
    else:
        print("Error, no se permiten campos vacios")
        print("Verifique que los datos sean correctos")
        
def consultarProductos():
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT P.id, P.nombre, P.precio, P.cantidad, C.nombre FROM Producto P inner join Categoria C on P.categoria_id = C.id"
    resultado = cursor.execute(instruccionSQL)
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                Precio: {}
                Cantidad: {}
                Categoria: {}
                """.format(dato[0], dato[1], dato[2], dato[3], dato[4]))

def actualizarProducto():
    idf = int(input("Digite el ID del producto a actualizar: "))
    if (validarIdPrducto(idf)):
        print("El ID no existe en la base de datos")
        return
    nomf = input("Digite el nuevo nombre: ")
    preciof = int(input("Digite el nuevo precio: "))
    cantf = int(input("Digite la nueva cantidad: "))
    categf = input("Digite la nueva categoria: ")
    if (len(nomf) > 0 and len(categf) > 0 and cantf > 0 and preciof > 0):
        conn = db.connect("Inventario.db")
        cursor = conn.cursor()
        instruccionSQL = "UPDATE Producto SET nombre = ?, precio = ?, cantidad = ?, categoria_id = ? WHERE id = ?"
        cursor.execute(instruccionSQL, (nomf, preciof, cantf, categf, idf))
        conn.commit()
        conn.close()
        print("El registro se actualizo exitosamente")
    else:
        print("Error, no se permiten campos vacios")
        print("Verifique que los datos sean correctos")
        
def eliminarProducto():
    idf = int(input("Digite el ID del producto a eliminar: "))
    if (validarIdPrducto(idf)):
        print("El ID no existe en la base de datos")
        return
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "DELETE FROM Producto WHERE id = ?"
    cursor.execute(instruccionSQL, (idf,))
    conn.commit()
    conn.close()
    print("El registro se elimino exitosamente")

def consultarProductoId():
    idf = int(input("Digite el ID del producto a consultar: "))
    if (validarIdPrducto(idf)):
        print("El ID no existe en la base de datos")
        return
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT P.id, P.nombre, P.precio, P.cantidad, C.nombre FROM Producto P inner join Categoria C on P.categoria_id = C.id WHERE P.id = ?"
    resultado = cursor.execute(instruccionSQL, (idf,))
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                Precio: {}
                Cantidad: {}
                Categoria: {}
                """.format(dato[0], dato[1], dato[2], dato[3], dato[4]))
    conn.close()

def consultarProductoNombre():
    nomf = input("Digite el nombre del producto a consultar: ")
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT P.id, P.nombre, P.precio, P.cantidad, C.nombre FROM Producto P inner join Categoria C on P.categoria_id = C.id WHERE P.nombre LIKE ?"
    resultado = cursor.execute(instruccionSQL, (f"%{nomf}%",))
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                Precio: {}
                Cantidad: {}
                Categoria: {}
                """.format(dato[0], dato[1], dato[2], dato[3], dato[4]))
    conn.close()

def consultarProductoCategoria():
    consultarCategoria()
    categf = input("Digite el id de la categoria del producto a consultar: ")
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT P.id, P.nombre, P.precio, P.cantidad, C.nombre FROM Producto P inner join Categoria C on P.categoria_id = C.id WHERE P.categoria_id = ?"
    resultado = cursor.execute(instruccionSQL, (categf,))
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                Precio: {}
                Cantidad: {}
                Categoria: {}
                """.format(dato[0], dato[1], dato[2], dato[3], dato[4]))
    conn.close()

def consultarProductoRangoPrecio():
    minf = int(input("Digite el precio minimo: "))
    maxf = int(input("Digite el precio maximo: "))
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT P.id, P.nombre, P.precio, P.cantidad, C.nombre FROM Producto P inner join Categoria C on P.categoria_id = C.id WHERE P.precio BETWEEN ? AND ?"
    resultado = cursor.execute(instruccionSQL, (minf, maxf))
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                Precio: {}
                Cantidad: {}
                Categoria: {}
                """.format(dato[0], dato[1], dato[2], dato[3], dato[4]))
    conn.close()